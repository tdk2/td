
#
class BSTree:
    # initialize the bst by a list of elements
    def __init__(self, lst=[], cmp=lambda x, y: x < y):
        self.__root = None
        self.__cmp = cmp
        for elem in lst:
            self.insert(elem)

    # add an element to the bst
    def insert(self, key):
        if self.__root != None:
            y = None
            x = self.__root
            while x != None:
                y = x
                if self.__cmp(key, x[BSTree.__KeyIndex]):
                    x = self.__getLeftChild(x)
                else:
                    x = self.__getRightChild(x)

            appendedNode = self.__createNode(key)
            appendedNode[BSTree.__ParentIndex] = y
            if self.__cmp(key, y[BSTree.__KeyIndex]):
                y[BSTree.__LeftChildIndex] = appendedNode
            else:
                y[BSTree.__RightChildIndex] = appendedNode

        else:
            self.__root = self.__createNode(key)

    
    # remove an item corresponding to the key from the BST
    def remove(self, key):
        if key == None:
            # key cannot be a null
            return None
        
        # try to find a node corresponding to the key
        node = self.__search(self.__root, key)
        if node == None:
            #nothing to do
            return None

        left, right = self.__getLeftChild(node), self.__getRightChild(node)
        if left == None or right == None:
            y = node
        else:
            # either successor or predecessor will do here
            y = self.__findPredecessor(node)

        #todo: check that y has at most one child

        leftY, rightY = self.__getLeftChild(y), self.__getRightChild(y)
        if leftY != None:
            x = leftY
        else:
            x = rightY

        if x != None:
            x[BSTree.__ParentIndex] = y[BSTree.__ParentIndex]

        if y[BSTree.__ParentIndex] == None:
            #y was the root
            self.__root = x
        else:
            parentY = self.__getParent(y)
            childIndex = BSTree.__RightChildIndex
            if y == self.__getLeftChild(parentY):
                childIndex = BSTree.__LeftChildIndex
            #todo: verify that y is right child of parentY [consistency check]
            elif y != self.__getRightChild(parentY):
                    raise "Unexpected error"
            parentY[childIndex] = x

        if y != node:
            node[BSTree.__KeyIndex] = y[BSTree.__KeyIndex]

        return self.__getKey(y)


    #printing content of the bst in sorted order
    def inorderWalk(self):
        print "<",
        self.__inorderWalk(self.__root)
        #printing newline
        print ">"

    # private section

    # creating a new node, all the links are set to None
    def __createNode(self, key):
        return [key, None, None, None]

    # aux util returning link to a child or parent or key
    def __getLink(self, node, linkIndex):
        if node != None:
            return node[linkIndex]
        else:
            return None

    # get key of the node
    def __getKey(self, node):
        return self.__getLink(node, BSTree.__KeyIndex)

    #
    def __getLeftChild(self, node):
        return self.__getLink(node, BSTree.__LeftChildIndex)

    #
    def __getRightChild(self, node):
        return self.__getLink(node, BSTree.__RightChildIndex)

    #
    def __getParent(self, node):
        return self.__getLink(node, BSTree.__ParentIndex)

    # recursive algorithm printing sorted keys
    def __inorderWalk(self, root):
        if root != None:
            self.__inorderWalk(root[BSTree.__LeftChildIndex])
            print root[BSTree.__KeyIndex],
            self.__inorderWalk(root[BSTree.__RightChildIndex])

    # TREE_SUCCESSOR
    def __findSuccessor(self, node):
        right =  self.__getRightChild(node)
        if right != None:
            return self.__findMinimumNode(right)

        y = self.__getParent(node)
        x = node
        while y != None and x == self.__getRightChild(y):
            x = y
            y = self.__getParent(y)

    # TREE_PREDECESSOR
    def __findPredecessor(self, node):
        left =  self.__getLeftChild(node)
        if left != None:
            return self.__findMaximumNode(left)

        y = self.__getParent(node)
        x = node
        while y != None and x == self.__getLeftChild(y):
            x = y
            y = self.__getParent(y)

    # find the leftmost node in the tree specified by root
    def __findMinimumNode(self, root):
        left = self.__getLeftChild(root)
        if left != None:
            return self.__findMinimumNode(left)
        else:
            return root

    # find the rightmost node in the tree specified by root
    def __findMaximumNode(self, root):
        right = self.__getRightChild(root)
        if right != None:
            return self.__findMaximumNode(right)
        else:
            return root

    # returns node corresponding to the key if it exists in the tree with root 
    def __search(self, root, key):
        if root == None or key == None:
            return None

        rootKey = self.__getKey(root)
        if key == rootKey:
            return root
        if self.__cmp(key, rootKey):
            # recursive search in the left subree
            return self.__search(self.__getLeftChild(root), key)
        else:
            # further search in right subreee
            return self.__search(self.__getRightChild(root), key)

    __KeyIndex = 0
    __LeftChildIndex = 1
    __RightChildIndex = 2
    __ParentIndex = 3


if __name__=="__main__":
    bst = BSTree([3, 1, 8, 2, 6, 7, 5], lambda x, y: x > y)
    bst.inorderWalk()
    bst.remove(8)
    bst.inorderWalk()
    bst.remove(6)
    bst.inorderWalk()
    bst.remove(3)
    bst.inorderWalk()
    bst.remove(1)
    bst.inorderWalk()
    bst.remove(5)
    bst.inorderWalk()
    bst.remove(7)
    bst.inorderWalk()
    bst.remove(2)
    bst.inorderWalk()

