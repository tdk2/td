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

