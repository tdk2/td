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

            # leaf node
            if (item[BSTree.LeftChildIndex] == nil or item[BSTree.RightChildIndex] == nil):
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
        color = item[BSTree.ColorIndex]
        if stage == 0:

            # 4th rule check: a red node must contain only black children
            if color == Color.Red:
                children = [item[BSTree.LeftChildIndex], item[BSTree.RightChildIndex]]
                colors = [item[BSTree.ColorIndex] for item in children]
                if colors.count(Color.Red) > 0:
                    self.__properties[3] = False

        elif stage == 1:
            #root node is checked against second property: the root must be black
            if item[BSTree.ParentIndex] == nil:
                if color != Color.Black:
                    self.__properties[1] = False

            #regular node must be either black or red (1st rule)
            if color != Color.Black and color != Color.Red:
                self.__properties[0] = False

            # leaf node
            if (item[BSTree.LeftChildIndex] == nil or item[BSTree.RightChildIndex] == nil):
                # calculate black nodes number
                node = item
                blacks = 0
                while node != nil:
                    blacks += 1 if node[BSTree.ColorIndex] == Color.Black else 0
                    node = node[BSTree.ParentIndex]

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


#
class BSTree:
    # initialize the bst by a list of elements
    def __init__(self, lst=[], cmp=lambda x, y: x < y):
        self.__cmp = cmp
        self.__nil = [None, None, None, None, Color.Black]
        self.__root = self.__nil
        for elem in lst:
            self.insert(elem)

    # add an element to the bst
    def insert(self, key):
        if self.__root != self.__nil:
            y = self.__nil
            x = self.__root
            while x != self.__nil:
                y = x
                if self.__cmp(key, x[BSTree.KeyIndex]):
                    x = self.__getLeftChild(x)
                else:
                    x = self.__getRightChild(x)

            appendedNode = self.__createNode(key, Color.Black)
            appendedNode[BSTree.ParentIndex] = y
            if self.__cmp(key, y[BSTree.KeyIndex]):
                y[BSTree.LeftChildIndex] = appendedNode
            else:
                y[BSTree.RightChildIndex] = appendedNode

        else:
            self.__root = self.__createNode(key, Color.Black)

    
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

        left, right = self.__getLeftChild(node), self.__getRightChild(node)
        if left == self.__nil:
            self.__transplant(node, right)
        elif right == self.__nil:
            self.__transplant(node, left)
        else:
            y = self.__findSuccessor(node)
            if y[BSTree.ParentIndex] != node:
                self.__transplant(y, y[BSTree.RightChildIndex])
                y[BSTree.RightChildIndex] = node[BSTree.RightChildIndex]
                y[BSTree.RightChildIndex][BSTree.ParentIndex] = y

            self.__transplant(node, y)
            y[BSTree.LeftChildIndex] = node[BSTree.LeftChildIndex]
            y[BSTree.LeftChildIndex][BSTree.ParentIndex] = y


    #printing content of the bst in sorted order
    def printInorder(self):
        #command = lambda root: return root[BSTree.KeyIndex]
        print "<",
        self.__inorderWalk(self.__root, self.__printItem)
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
        print "RBT consistency: ", visitor.success()


    # private section

    # creating a new node, all the links are set to None
    def __createNode(self, key, color):
        return [key, self.__nil, self.__nil, self.__nil, color]

    # aux util returning link to a child or parent or key
    def __getLink(self, node, linkIndex):
        if node != self.__nil:
            return node[linkIndex]
        else:
            return self.__nil

    # get key of the node
    def __getKey(self, node):
        return self.__getLink(node, BSTree.KeyIndex)

    #
    def __getLeftChild(self, node):
        return self.__getLink(node, BSTree.LeftChildIndex)

    #
    def __getRightChild(self, node):
        return self.__getLink(node, BSTree.RightChildIndex)

    #
    def __getParent(self, node):
        return self.__getLink(node, BSTree.ParentIndex)

 
    # TREE_SUCCESSOR
    def __findSuccessor(self, node):
        right =  self.__getRightChild(node)
        if right != self.__nil:
            return self.__findMinimumNode(right)

        y = self.__getParent(node)
        x = node
        while y != self.__nil and x == self.__getRightChild(y):
            x = y
            y = self.__getParent(y)

    # TREE_PREDECESSOR
    def __findPredecessor(self, node):
        left =  self.__getLeftChild(node)
        if left != self.__nil:
            return self.__findMaximumNode(left)

        y = self.__getParent(node)
        x = node
        while y != self.__nil and x == self.__getLeftChild(y):
            x = y
            y = self.__getParent(y)

    # find the leftmost node in the tree specified by root
    def __findMinimumNode(self, root):
        left = self.__getLeftChild(root)
        if left != self.__nil:
            return self.__findMinimumNode(left)
        else:
            return root

    # find the rightmost node in the tree specified by root
    def __findMaximumNode(self, root):
        right = self.__getRightChild(root)
        if right != self.__nil:
            return self.__findMaximumNode(right)
        else:
            return root

    # auxiliary algorithm that is used in deletion procedure
    # note: introduced in third edition of the book
    def __transplant(self, u, v):
        uParent = self.__getParent(u)
        if uParent == self.__nil:
            self.__root = v
        elif self.__getLeftChild(uParent) == u:
            uParent[BSTree.LeftChildIndex] = v
        else:
            uParent[BSTree.RightChildIndex] = v
        if v != self.__nil:
            v[BSTree.ParentIndex] = uParent

    # returns node corresponding to the key if it exists in the tree with root 
    def __search(self, root, key):
        if root == self.__nil or key == self.__nil:
            return self.__nil

        rootKey = self.__getKey(root)
        if key == rootKey:
            return root
        if self.__cmp(key, rootKey):
            # recursive search in the left subree
            return self.__search(self.__getLeftChild(root), key)
        else:
            # further search in right subreee
            return self.__search(self.__getRightChild(root), key)

    # just printing an item
    def __printItem(self, item, stage, nil):
        if stage == 1:
            print item[BSTree.KeyIndex],


    # inorder walk
    def __inorderWalk(self, root, command):
        if root != self.__nil:
            command(root, 0, self.__nil)
            self.__inorderWalk(root[BSTree.LeftChildIndex], command)
            command(root, 1, self.__nil)
            self.__inorderWalk(root[BSTree.RightChildIndex], command)
            command(root, 2, self.__nil)

    KeyIndex = 0
    LeftChildIndex = 1
    RightChildIndex = 2
    ParentIndex = 3
    ColorIndex = 4

if __name__=="__main__":
    #values = [3, 1, 8, 2, 6, 7, 5]
    values = [3, 1, 8]
    bst = BSTree(values, lambda x, y: x < y)
    bst.printStatistics()                                        
    bst.checkRBT()    

    MinPow = 6
    MaxPow = 14
    values = [utils.Random(0, 2**MaxPow) for x in xrange(2**MaxPow)]
    for bstSize in xrange(MinPow, MaxPow+1):
        #values = [utils.Random(0, 1000) for x in xrange(2**bstSize)]
        range = values[0:2**bstSize]
        bst = BSTree(range, lambda x, y: x < y)
        bst.printStatistics()
        bst.checkRBT()

        permutation = utils.RandomPermutation(range)
        for delItem in permutation[0:len(permutation)-10]:
            bst.remove(delItem)
        bst.printInorder()


