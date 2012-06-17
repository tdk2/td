'''
Graph library
'''
 
class Node:
    def __init__(self, name):
        self.name = name
        self.adj = []


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
        #to[1].append(fr)

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

    
class Color:
    White = 0
    Gray = 1
    Black = 2

def DFS_Visit(node, onFinished):
    node.color = Color.Gray
    for adjNode in node.adj:
        if adjNode.color == Color.White:
            DFS_Visit(adjNode, onFinished)
    node.color = Color.Black
    onFinished(node)


def DFS(graph, onFinished):
    for node in graph.nodes:
        node.color = Color.White 

    for node in graph.nodes:
        if node.color == Color.White:
            DFS_Visit(node, onFinished) 


def sortTopologically(dag):
    sortedNodes = []
    onFinishedCallback = lambda node: sortedNodes.insert(0, node)
    DFS(dag, onFinishedCallback)
    dag.nodes = sortedNodes


def countPaths(dag, nodeFrom, nodeTo):
    if nodeFrom == nodeTo:
        return 1

    sortTopologically(dag)
    fromIndex = -1
    toIndex = -1
    index = 0
    for node in dag.nodes:
        node.pathcount = 0
        node.paths = []
        if node.name == nodeFrom:
            fromIndex = index
            node.pathcount = 1
            node.paths.append(node.name + "->")
        elif node.name == nodeTo:
            toIndex = index
        index = index+1
    if fromIndex == -1 or toIndex == -1:
        print "At least one of the nodes wasn't found in the graph specified"
        return 0
    if fromIndex > toIndex:
        print "%s is topologically greater than %s" % (str(nodeFrom), str(nodeTo))
        return 0
    for node in dag.nodes[fromIndex:toIndex]:
        for adjNode in node.adj:
            adjNode.pathcount = adjNode.pathcount + node.pathcount
            for path in node.paths:
                adjNode.paths.append(path + adjNode.name + "->")
    print dag.nodes[toIndex].paths
    return dag.nodes[toIndex].pathcount
