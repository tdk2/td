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

# Verifies AVL properties
class AVLTreeCheck:
    def __call__(self, item, stage, nil):
        if stage == 0:
           height = item.Height
           rightHeight = AVLTreeNode.getRightHeight(item)
           leftHeight = AVLTreeNode.getLeftHeight(item)
           if height != max(rightHeight, leftHeight) or (height - min(rightHeight, leftHeight)) > 1:
               print "violation of AVL properties at node %d:%d, leftHeight %d, rightHeight %d" % (item.Key, item.Height, leftHeight, rightHeight) 


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

    @staticmethod
    def getLeftHeight(node):
        if node == None:
            return -1
        if node.Left == None:
            return 0
        else:
            return node.Left.Height+1

    @staticmethod
    def getRightHeight(node):
        if node == None:
            return -1
        if node.Right == None:
            return 0
        else:
            return node.Right.Height+1

    @staticmethod
    def getNodeHeight(node):
        if node != None:
            return node.Height
        else:
            return -1

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

        #print "removing %d:%d" % (node.Key, node.Height)
        if node.Left == None:
            x = node.Right
            z = node.Parent
            self.__transplant(node, x)
        elif node.Right == None:
            x = node.Left
            z = node.Parent
            self.__transplant(node, x)
        else:
            y = self.__findSuccessor(node)
            x = y.Right
            if y.Parent == node:
                #the line below forces child-parent consistency even if y.Right is sentinel 
                #x.Parent = y
                z = y
                pass
            else:
                z = y.Parent
                self.__transplant(y, y.Right)
                y.Right = node.Right
                y.Right.Parent = y

            self.__transplant(node, y)
            y.Left = node.Left
            y.Left.Parent = y

        #updating height attributes
        self.__avlDeleteFixup(z)
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
        visitor = AVLTreeCheck()
        self.__inorderWalk(self.__root, visitor)


    # private section


    def __avlInsertFixup(self, z):
        #updating height attributes
        self.__recalculateHeightUp(z.Parent)

        #search for avl violation and fixit
        if z.Parent == None or z.Parent.Parent == None:
            return

        node = z.Parent.Parent
        while node != None:
            factor = self.__avlFactor(node)
            if abs(factor) > 2:
                #exception
                print "WAT?!!!"
            if abs(factor) > 1:
                #print "fixing", factor
                if factor > 0:
                    if self.__avlFactor(node.Left) < 0:
                       self.__leftRotate(node.Left)
                    self.__rightRotate(node)
                else:
                    if self.__avlFactor(node.Right) > 0:
                       self.__rightRotate(node.Right)
                    self.__leftRotate(node)
                break
            node = node.Parent

    def __avlDeleteFixup(self, z):
        if z == None:
            z = self.__root
        #print "%d:%d" % (z.Key, z.Height)
        self.__recalculateHeightUp(z, 1000)
        node = z
        while node != None:
            factor = self.__avlFactor(node)
            if abs(factor) > 2:
                #exception
                print "WAT?!!!"
            if abs(factor) > 1:
                #print "fixing", factor
                nextNode = node.Parent
                if factor > 0:
                    if self.__avlFactor(node.Left) < 0:
                       self.__leftRotate(node.Left)
                    self.__rightRotate(node)
                else:
                    if self.__avlFactor(node.Right) > 0:
                       self.__rightRotate(node.Right)
                    self.__leftRotate(node)
                node = nextNode
            else:
                #print node.Key, node.Parent.Key
                node = node.Parent


    #return difference between left and right heights
    #e.g. -2 means right height is longer than left height by 2
    def __avlFactor(self, z):
        if (z == None):
            return 0
        return  AVLTreeNode.getLeftHeight(z) - AVLTreeNode.getRightHeight(z)


    # LEFT-ROTATE
    def __leftRotate(self, x):
        y = x.Right
        x.Right = y.Left
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
        self.__recalculateHeightUp(x, 3)

    # RIGHT-ROTATE
    def __rightRotate(self, y):
        x = y.Left
        y.Left = x.Right
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
        self.__recalculateHeightUp(y, 3)
 
    # update heights up
    def __recalculateHeightUp(self, node, forceMinUpdate = 1):
        while node != None:
            newNodeHeight = max(AVLTreeNode.getNodeHeight(node.Left), AVLTreeNode.getNodeHeight(node.Right))+1
            if newNodeHeight != node.Height or forceMinUpdate > 0:
                forceMinUpdate -= 1
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
        if v != None:
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

def testSingle():
    #values = [3, 1, 8, 2, 6, 7, 5]
    #values = [9, 5, 6, 6, 9, 13, 15, 13, 6, 0, 13, 4, 6, 15, 0, 7]
    values = [15, 14, 19, 17, 27, 5, 28, 11, 19, 29, 6, 0, 29, 31, 15, 14, 28, 1, 8, 23, 2, 26, 28, 19, 13, 10, 28, 32, 2, 30, 21, 21]
    #values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bst = AVLTree(values, lambda x, y: x < y)
    bst.printStatistics()
    bst.printInorder()
    bst.checkAVL()
    bst.remove(values[0])
    bst.checkAVL()

def testMultiple():
    MinPow = 6
    MaxPow = 16
    values = [utils.Random(0, 2**MaxPow) for x in xrange(2**MaxPow)]
    for bstSize in xrange(MinPow, MaxPow+1):
        range = values[0:2**bstSize]
        bst = AVLTree(range, lambda x, y: x < y)
        bst.printStatistics()
        #bst.printInorder()
        #print range

        bst.remove(values[0])
        #permutation = utils.RandomPermutation(range)
        #for delItem in permutation[0:len(permutation)-10]:
        #    bst.remove(delItem)
        bst.checkAVL()
        #bst.printInorder()

if __name__=="__main__":
    #testSingle()
    testMultiple()

