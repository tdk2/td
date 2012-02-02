import sys
sys.path.append(sys.path[0] + '/../hash')
import utils

# collect element number
class TreeElementNumberCollector:
    def __init__(self):
        self.__number = 0

    def __call__(self, item, stage, nil):
        if stage == 1:
            self.__number = self.__number + 1

    def getValue(self):
        return self.__number


# collect element number
class TreeElementHeightCollector:
    def __init__(self):
        self.__current = 0
        self.__max = 0
        self.__min = None

    def __call__(self, item, stage, nil):
        if stage == 0:
            self.__current = self.__current + 1
        elif stage == 1:
            self.__max = max(self.__max, self.__current)

            #child-parent consistency check
            if item.Left != nil and item.Left.Parent != item:
               print "Left child has different parent!"
            if item.Right != nil and item.Right.Parent != item:
               print "Right child has different parent!"
            if item.Parent != nil and item.Parent.Left != item and item.Parent.Right != item:
               print "Parent has not the item as a child!"

            # leaf node
            if (item.Left == nil or item.Right == nil):
                if self.__min == None:
                    self.__min = self.__max
                self.__min = min(self.__min, self.__current)

        elif stage == 2:
            self.__current = self.__current - 1

    def getHeights(self):
        return {"max":self.__max, "min":self.__min};

# Verifies RBT properties
class RBTreeCheck:
    def __init__(self):
        self.__properties = [True for x in xrange(5)]
        self.__blacksNumber = None

    def __call__(self, item, stage, nil):
        color = item.Color
        if stage == 0:

            # 4th rule check: a red node must contain only black children
            if color == Color.Red:
                children = [item.Left, item.Right]
                colors = [item.Color for item in children]
                if colors.count(Color.Red) > 0:
                    self.__properties[3] = False

        elif stage == 1:
            #root node is checked against second property: the root must be black
            if item.Parent == nil:
                if color != Color.Black:
                    self.__properties[1] = False

            #regular node must be either black or red (1st rule)
            if color != Color.Black and color != Color.Red:
                self.__properties[0] = False

            # leaf node
            if (item.Left == nil or item.Right == nil):
                # calculate black nodes number
                node = item
                blacks = 0
                while node != nil:
                    blacks += 1 if node.Color == Color.Black else 0
                    node = node.Parent

                if self.__blacksNumber == None:
                    self.__blacksNumber = blacks
                if blacks != self.__blacksNumber:
                    # 5th rule is violated
                    self.__properties[4] = False

        elif stage == 2:
            pass

    def success(self):
        return self.__properties;

# generic visitor
class TreeElementVisitor:
    def __init__(self, visitors):
        self.__visitors = visitors

    def __call__(self, item, stage, nil):
        for visitor in self.__visitors :
            visitor(item, stage, nil)



class AVLTreeNode:
    def __init__(self, key, height = 0):
        self.Key = key
        self.Height = height
        self.Left = None
        self.Right = None
        self.Parent = None


#
class AVLTree:
    # initialize the bst by a list of elements
    def __init__(self, lst=[], cmp=lambda x, y: x < y):
        self.__cmp = cmp
        self.__root = None
        for elem in lst:
            self.insert(elem)

    # add an element to the bst
    def insert(self, key):
        z = AVLTreeNode(key)
        y = None
        x = self.__root
        while x != None:
            y = x
            if self.__cmp(key, x.Key):
                x = x.Left
            else:
                x = x.Right

        z.Parent = y
        if y == None:
            #z.Color = Color.Black
            self.__root = z
        elif self.__cmp(key, y.Key):
            y.Left = z
        else:
            y.Right = z

        #updating height attributes
        node = z.Parent
        offset = 0
        while node != None:
            offset += 1
            node.Height = max(node.Height, offset)
            node = node.Parent
        self.__avlInsertFixup(z)

    
    # remove an item corresponding to the key from the BST
    def remove(self, key):
        if key == None:
            # key cannot be a null
            return
        
        # try to find a node corresponding to the key
        node = self.__search(self.__root, key)
        if node == None:
            #nothing to do
            return

        if node.Left == None:
            x = node.Right
            self.__transplant(node, x)
        elif node.Right == None:
            x = node.Left
            self.__transplant(node, x)
        else:
            y = self.__findSuccessor(node)
            x = y.Right
            if y.Parent == node:
                #the line below forces child-parent consistency even if y.Right is sentinel 
                x.Parent = y
            else:
                self.__transplant(y, y.Right)
                y.Right = node.Right
                y.Right.Parent = y

            self.__transplant(node, y)
            y.Left = node.Left
            y.Left.Parent = y

        #if yColor == Color.Black:
        #    self.__rbDeleteFixup(x)


    #printing content of the bst in sorted order
    def printInorder(self):
        print "<",
        for item in self.__inorderWalkGeneration(self.__root):
            print "%d:%d" % (item.Key, item.Height),
        #printing newline
        print ">"

    def printStatistics(self):
        sizeCollector = TreeElementNumberCollector()
        heightCollector = TreeElementHeightCollector()
        visitor = TreeElementVisitor([sizeCollector, heightCollector])
        self.__inorderWalk(self.__root, visitor)
        print "size: %d, heights: " % sizeCollector.getValue(), heightCollector.getHeights()

    def checkAVL(self):
        pass
#       visitor = RBTreeCheck()
#       self.__inorderWalk(self.__root, visitor)
#       result = visitor.success()
#       #check if Rule3 is not violated
#       if None.Color != Color.Black:
#           result[2] = False
#       print "RBT consistency: ", result


    # private section


    def __avlInsertFixup(self, z):
        #search for avl violation and fixit
        if z.Parent == None or z.Parent.Parent == None:
            return

        node = z.Parent.Parent
        while node != None:
            childIdx, heightDiff = self.__avlHeightDifference(node)
            if heightDiff > 2:
                #exception
                print "WAT?!!!"
            if heightDiff > 1:
                print "fixing", childIdx, heightDiff
                if childIdx == 0:
                    self.__rightRotate(node)
                else:
                    self.__leftRotate(node)
                break
            node = node.Parent

    #return index of a child index (Left is 0, Right is 1) which height is longer than of its sibling
    #also non-negative height difference is returned
    #e.g. (0, 2) means avl height violation: the left height is bigger than right by two
    def __avlHeightDifference(self, z):
        if (z == None):
            return (0, 0)
        leftHeight, rightHeight = self.__getLeftHeight(z), self.__getRightHeight(z)
        if leftHeight > rightHeight:
            return (0, leftHeight - rightHeight)
        else:
            return (1, rightHeight - leftHeight)

    def __getLeftHeight(self, z):
        if z == None:
            return -1
        if z.Left == None:
            return 0
        else:
            return z.Left.Height+1

    def __getRightHeight(self, z):
        if z == None:
            return -1
        if z.Right == None:
            return 0
        else:
            return z.Right.Height+1

    def __getNodeHeight(self, z):
        if z != None:
            return z.Height
        else:
            return -1

    # LEFT-ROTATE
    def __leftRotate(self, x):
        y = x.Right
        x.Right = y.Left
        alfaHeight = self.__getNodeHeight(x.Left)
        betaHeight = self.__getNodeHeight(y.Left)
        gammaHeight = self.__getNodeHeight(y.Right)
        if y.Left != None:
            y.Left.Parent = x
        y.Parent = x.Parent
        if x.Parent == None:
            self.__root = y
        elif x.Parent.Left == x:
            x.Parent.Left = y
        else:
            x.Parent.Right = y
        y.Left = x
        x.Parent = y
        x.Height = max(alfaHeight, betaHeight)+1
        y.Height = max(x.Height, gammaHeight)+1
        self.__recalculateHeightUp(y.Parent)

    # RIGHT-ROTATE
    def __rightRotate(self, y):
        x = y.Left
        y.Left = x.Right
        alfaHeight = self.__getNodeHeight(x.Left)
        betaHeight = self.__getNodeHeight(x.Right)
        gammaHeight = self.__getNodeHeight(y.Right)
        if x.Right != None:
            x.Right.Parent = y
        x.Parent = y.Parent
        if y.Parent == None:
            self.__root = x
        elif y.Parent.Left == y:
            y.Parent.Left = x
        else:
            y.Parent.Right = x
        x.Right = y
        y.Parent = x
        y.Height = max(betaHeight, gammaHeight)+1
        x.Height = max(alfaHeight, y.Height)+1
        self.__recalculateHeightUp(x.Parent)
 
    # update heights up
    def __recalculateHeightUp(self, node):
        while node != None:
            newNodeHeight = max(self.__getNodeHeight(node.Left), self.__getNodeHeight(node.Right))+1
            if newNodeHeight != node.Height:
                node.Height = newNodeHeight
                node = node.Parent
            else:
                node = None

    # TREE_SUCCESSOR
    def __findSuccessor(self, node):
        right =  node.Right
        if right != None:
            return self.__findMinimumNode(right)

        y = node.Parent
        x = node
        while y != None and x == y.Right:
            x = y
            y = y.Parent

    # TREE_PREDECESSOR
    def __findPredecessor(self, node):
        left =  node.Left
        if left != None:
            return self.__findMaximumNode(left)

        y = node.Parent
        x = node
        while y != None and x == y.Left:
            x = y
            y = y.Parent

    # find the leftmost node in the tree specified by root
    def __findMinimumNode(self, root):
        left = root.Left
        if left != None:
            return self.__findMinimumNode(left)
        else:
            return root

    # find the rightmost node in the tree specified by root
    def __findMaximumNode(self, root):
        right = root.Right
        if right != None:
            return self.__findMaximumNode(right)
        else:
            return root

    # auxiliary algorithm that is used in deletion procedure
    # note: introduced in third edition of the book
    def __transplant(self, u, v):
        uParent = u.Parent
        if uParent == None:
            self.__root = v
        elif uParent.Left == u:
            uParent.Left = v
        else:
            uParent.Right = v
        v.Parent = uParent

    # returns node corresponding to the key if it exists in the tree with root 
    def __search(self, root, key):
        if root == None or key == None:
            return None

        if key == root.Key:
            return root
        if self.__cmp(key, root.Key):
            # recursive search in the left subree
            return self.__search(root.Left, key)
        else:
            # further search in right subreee
            return self.__search(root.Right, key)


    # inorder walk
    def __inorderWalk(self, root, command):
        if root != None:
            command(root, 0, None)
            self.__inorderWalk(root.Left, command)
            command(root, 1, None)
            self.__inorderWalk(root.Right, command)
            command(root, 2, None)

    # inorder walk for generators
    def __inorderWalkGeneration(self, root):
        if root != None:
            for item in self.__inorderWalkGeneration(root.Left):
                yield item
            yield root
            for item in self.__inorderWalkGeneration(root.Right):
                yield item

if __name__=="__main__":
    values = [3, 1, 8, 2, 6, 7, 5]
    values = [3, 1, 8, 2, 6, 7]
    #values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bst = AVLTree(values, lambda x, y: x < y)
    bst.printStatistics()
    bst.printInorder()
    bst.checkAVL()

#   MinPow = 6
#   MaxPow = 12
#   values = [utils.Random(0, 2**MaxPow) for x in xrange(2**MaxPow)]
#   for bstSize in xrange(MinPow, MaxPow+1):
#       range = values[0:2**bstSize]
#       bst = AVLTree(range, lambda x, y: x < y)
#       bst.printStatistics()
#
#       permutation = utils.RandomPermutation(range)
#       for delItem in permutation[0:len(permutation)-10]:
#           bst.remove(delItem)
#       bst.checkRBT()
#       bst.printInorder()

