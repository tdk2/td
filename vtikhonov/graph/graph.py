'''
Graph library
'''
 
class Node:
    def __init__(self, name):
        self.name = name
        self.adj = []


class UDGraph:

    def __init__(self, name = ""):
        self.name = name
        self.nodes = []

    def addNode(self, nodeName):
        for node in self.nodes:
            if node.name == nodeName:
                return node
        newNode = Node(nodeName)
        self.nodes.append(newNode)
        return newNode

    def addEdge(self, nodeFrom, nodeTo):
        if nodeFrom == nodeTo:
            # self loops are forbidden for undirected graph
            raise "Self loops are forbidden"
        fr = self.__getOrCreateNode(nodeFrom)
        to = self.__getOrCreateNode(nodeTo)
        if not to in fr.adj:
            fr.adj.append(to)
        if not fr in to.adj:
            to.adj.append(fr)

    def printGraph(self):
        print "[%s]" % str(self.name)
        for node in self.nodes:
            print node.name, ": ",
            for adj in node.adj:
                print adj.name, ",",
            print

    #private
    def __getOrCreateNode(self, nodeName):
        for node in self.nodes :
            if node.name == nodeName:
                return node
        return self.addNode(nodeName)

   
class DiGraph:

    def __init__(self, name = ""):
        self.name = name
        self.nodes = []

    def addNode(self, node):
        newNode = Node(node)
        self.nodes.append(newNode)
        return newNode

    def addEdge(self, nodeFrom, nodeTo):
        fr = self.__getOrCreateNode(nodeFrom)
        to = self.__getOrCreateNode(nodeTo)
        fr.adj.append(to)

    def printGraph(self):
        print "[%s]" % str(self.name)
        for node in self.nodes:
            print node.name, ": ",
            for adj in node.adj:
                print adj.name, ",",
            print

    #private
    def __getOrCreateNode(self, nodeName):
        for node in self.nodes :
            if node.name == nodeName:
                return node
        return self.addNode(nodeName)

   
