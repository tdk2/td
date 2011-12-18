
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
                    x = x[BSTree.__LeftChild]
                else:
                    x = x[BSTree.__RightChild]

            appendedNode = [key, None, None]
            if self.__cmp(key, y[BSTree.__KeyIndex]):
                y[BSTree.__LeftChild] = appendedNode
            else:
                y[BSTree.__RightChild] = appendedNode

        else:
            self.__root = [key, None, None]


    def inorderWalk(self):
        self.__inorderWalk(self.__root)

    # private
    def __inorderWalk(self, root):
        if root != None:
            self.__inorderWalk(root[BSTree.__LeftChild])
            print root[BSTree.__KeyIndex],
            self.__inorderWalk(root[BSTree.__RightChild])

    __KeyIndex = 0
    __LeftChild = 1
    __RightChild = 2


if __name__=="__main__":
    bst = BSTree([3, 1, 8, 2, 6, 7, 5], lambda x, y: x > y)
    bst.inorderWalk()
