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
        self.__number = 0
        self.__pathLenSum = 0

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
                self.__pathLenSum += self.__current
                self.__number = self.__number+1
                if self.__min == None:
                    self.__min = self.__max
                self.__min = min(self.__min, self.__current)

        elif stage == 2:
            self.__current = self.__current - 1

    def getHeights(self):
        return {"max":self.__max, "min":self.__min, "avg":self.__pathLenSum/max(self.__number, 1)};

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


class Color:
    Red = 'Red'
    Black = 'Black'


class BSTreeNode:
    def __init__(self, key, color, nil):
        self.Key = key
        self.Color = color
        self.Left = nil
        self.Right = nil
        self.Parent = nil


#
class BSTree:
    # initialize the bst by a list of elements
    def __init__(self, lst=[], cmp=lambda x, y: x < y):
        self.__cmp = cmp
        self.__nil = BSTreeNode(None, Color.Black, None)
        self.__root = self.__nil
        for elem in lst:
            self.insert(elem)

    # add an element to the bst
    def insert(self, key):
        z = self.__createNode(key, Color.Red)
        y = self.__nil
        x = self.__root
        while x != self.__nil:
            y = x
            if self.__cmp(key, x.Key):
                x = x.Left
            else:
                x = x.Right

        z.Parent = y
        if y == self.__nil:
            #z.Color = Color.Black
            self.__root = z
        elif self.__cmp(key, y.Key):
            y.Left = z
        else:
            y.Right = z

        self.__rbInsertFixup(z)

    
    # remove an item corresponding to the key from the BST
    def remove(self, key):
        if key == None:
            # key cannot be a null
            return
        
        # try to find a node corresponding to the key
        node = self.__search(self.__root, key)
        if node == self.__nil:
            #nothing to do
            return

        yColor = node.Color
        if node.Left == self.__nil:
            x = node.Right
            self.__transplant(node, x)
        elif node.Right == self.__nil:
            x = node.Left
            self.__transplant(node, x)
        else:
            y = self.__findSuccessor(node)
            x = y.Right
            yColor = y.Color
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
            y.Color = node.Color

        if yColor == Color.Black:
            self.__rbDeleteFixup(x)


    #printing content of the bst in sorted order
    def printInorder(self):
        print "<",
        for item in self.__inorderWalkGeneration(self.__root):
            print item.Key,
        #printing newline
        print ">"

    def printStatistics(self):
        sizeCollector = TreeElementNumberCollector()
        heightCollector = TreeElementHeightCollector()
        visitor = TreeElementVisitor([sizeCollector, heightCollector])
        self.__inorderWalk(self.__root, visitor)
        print "size: %d, heights: " % sizeCollector.getValue(), heightCollector.getHeights()

    def checkRBT(self):
        visitor = RBTreeCheck()
        self.__inorderWalk(self.__root, visitor)
        result = visitor.success()
        #check if Rule3 is not violated
        if self.__nil.Color != Color.Black:
            result[2] = False
        print "RBT consistency: ", result


    # private section

    # creating a new node, all the links are set to None
    def __createNode(self, key, color):
        return BSTreeNode(key, color, self.__nil)

    def __rbInsertFixup(self, z):
        while z.Parent.Color == Color.Red:
            if z.Parent == z.Parent.Parent.Left:
                y = z.Parent.Parent.Right
                if y.Color == Color.Red:
                    z.Parent.Color = Color.Black
                    y.Color = Color.Black
                    z.Parent.Parent.Color = Color.Red
                    z = z.Parent.Parent
                else:
                    if z == z.Parent.Right:
                        z = z.Parent
                        self.__leftRotate(z)
                    z.Parent.Color = Color.Black
                    z.Parent.Parent.Color = Color.Red
                    self.__rightRotate(z.Parent.Parent)
            else:
                # the same, change left-right
                y = z.Parent.Parent.Left
                if y.Color == Color.Red:
                    z.Parent.Color = Color.Black
                    y.Color = Color.Black
                    z.Parent.Parent.Color = Color.Red
                    z = z.Parent.Parent
                else:
                    if z == z.Parent.Left:
                        z = z.Parent
                        self.__rightRotate(z)
                    z.Parent.Color = Color.Black
                    z.Parent.Parent.Color = Color.Red
                    self.__leftRotate(z.Parent.Parent)

        self.__root.Color = Color.Black

    def __rbDeleteFixup(self, x):
        while x != self.__root and x.Color == Color.Black:
            if x == x.Parent.Left:
                w = x.Parent.Right
                if w.Color == Color.Red:
                    w.Color = Color.Black
                    x.Parent.Color = Color.Red
                    self.__leftRotate(x.Parent)
                    w = x.Parent.Right
                if w == self.__nil:
                    print "w is nil!!!"
                if w.Left.Color == Color.Black and w.Right.Color == Color.Black:
                    w.Color = Color.Red
                    x = x.Parent
                else:
                    if w.Right.Color == Color.Black:
                        w.Left.Color = Color.Black
                        w.Color = Color.Red
                        self.__rightRotate(w)
                        w = x.Parent.Right
                    w.Color = x.Parent.Color
                    x.Parent.Color = Color.Black
                    w.Right.Color = Color.Black
                    self.__leftRotate(x.Parent)
                    x = self.__root
            else:
                w = x.Parent.Left
                if w.Color == Color.Red:
                    w.Color = Color.Black
                    x.Parent.Color = Color.Red
                    self.__rightRotate(x.Parent)
                    w = x.Parent.Left
                if w.Right.Color == Color.Black and w.Left.Color == Color.Black:
                    w.Color = Color.Red
                    x = x.Parent
                else:
                    if w.Left.Color == Color.Black:
                        w.Right.Color = Color.Black
                        w.Color = Color.Red
                        self.__leftRotate(w)
                        w = x.Parent.Left
                    w.Color = x.Parent.Color
                    x.Parent.Color = Color.Black
                    w.Left.Color = Color.Black
                    self.__rightRotate(x.Parent)
                    x = self.__root
        x.Color = Color.Black


    # LEFT-ROTATE
    def __leftRotate(self, x):
        y = x.Right
        x.Right = y.Left
        if y.Left != self.__nil:
            y.Left.Parent = x
        y.Parent = x.Parent
        if x.Parent == self.__nil:
            self.__root = y
        elif x.Parent.Left == x:
            x.Parent.Left = y
        else:
            x.Parent.Right = y
        y.Left = x
        x.Parent = y

    # RIGHT-ROTATE
    def __rightRotate(self, y):
        x = y.Left
        y.Left = x.Right
        if x.Right != self.__nil:
            x.Right.Parent = y
        x.Parent = y.Parent
        if y.Parent == self.__nil:
            self.__root = x
        elif y.Parent.Left == y:
            y.Parent.Left = x
        else:
            y.Parent.Right = x
        x.Right = y
        y.Parent = x
 
    # TREE_SUCCESSOR
    def __findSuccessor(self, node):
        right =  node.Right
        if right != self.__nil:
            return self.__findMinimumNode(right)

        y = node.Parent
        x = node
        while y != self.__nil and x == y.Right:
            x = y
            y = y.Parent

    # TREE_PREDECESSOR
    def __findPredecessor(self, node):
        left =  node.Left
        if left != self.__nil:
            return self.__findMaximumNode(left)

        y = node.Parent
        x = node
        while y != self.__nil and x == y.Left:
            x = y
            y = y.Parent

    # find the leftmost node in the tree specified by root
    def __findMinimumNode(self, root):
        left = root.Left
        if left != self.__nil:
            return self.__findMinimumNode(left)
        else:
            return root

    # find the rightmost node in the tree specified by root
    def __findMaximumNode(self, root):
        right = root.Right
        if right != self.__nil:
            return self.__findMaximumNode(right)
        else:
            return root

    # auxiliary algorithm that is used in deletion procedure
    # note: introduced in third edition of the book
    def __transplant(self, u, v):
        uParent = u.Parent
        if uParent == self.__nil:
            self.__root = v
        elif uParent.Left == u:
            uParent.Left = v
        else:
            uParent.Right = v
        v.Parent = uParent

    # returns node corresponding to the key if it exists in the tree with root 
    def __search(self, root, key):
        if root == self.__nil or key == self.__nil:
            return self.__nil

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
        if root != self.__nil:
            command(root, 0, self.__nil)
            self.__inorderWalk(root.Left, command)
            command(root, 1, self.__nil)
            self.__inorderWalk(root.Right, command)
            command(root, 2, self.__nil)

    # inorder walk for generators
    def __inorderWalkGeneration(self, root):
        if root != self.__nil:
            for item in self.__inorderWalkGeneration(root.Left):
                yield item
            yield root
            for item in self.__inorderWalkGeneration(root.Right):
                yield item

if __name__=="__main__":
#    values = [3, 1, 8, 2, 6, 7, 5]
#   values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   bst = BSTree(values, lambda x, y: x < y)
#   bst.remove(9)
#   bst.printStatistics()
#   bst.printInorder()
#   bst.checkRBT()

    MinPow = 6
    MaxPow = 12
    values = [utils.Random(0, 2**MaxPow) for x in xrange(2**MaxPow)]
    for bstSize in xrange(MinPow, MaxPow+1):
        range = values[0:2**bstSize]
        bst = BSTree(range, lambda x, y: x < y)
        bst.printStatistics()

        permutation = utils.RandomPermutation(range)
        for delItem in permutation[0:len(permutation)-10]:
            bst.remove(delItem)
        bst.checkRBT()
        bst.printInorder()

