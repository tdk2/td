'''
Graph algorithms
'''

import graph

class Color:
    White = 0
    Gray = 1
    Black = 2

class DFS:
   def __init__(self, gr):
      self.graph = gr

   def run(self, onFinished):
      self.onFinished = onFinished
      self.counter = 0
      for node in self.graph.nodes:
         node.color = Color.White 

      for node in self.graph.nodes:
         if node.color == Color.White:
            self.visit(node) 


   def visit(self, node):
      self.counter = self.counter + 1
      node.discovered = self.counter
      node.backLow = node.discovered
      node.color = Color.Gray
      low = len(self.graph.nodes)*1000 + 1000
      for adjNode in node.adj:
         if adjNode.color == Color.White:
            #print "tree edge [%s - %s]" % (node.name, adjNode.name)
            self.visit(adjNode)
            low = min(low, adjNode.low, adjNode.backLow)
         elif adjNode.color == Color.Gray:
            node.backLow = min(node.backLow, adjNode.discovered)
      node.color = Color.Black
      self.counter = self.counter + 1
      node.finished = self.counter
      node.low = min(node.discovered, low)
      self.onFinished(node)



def sortTopologically(dag):
    sortedNodes = []
    onFinishedCallback = lambda node: sortedNodes.insert(0, node)
    dfs = DFS(dag)
    dfs.run(onFinishedCallback)
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


def printNode(node):
    print "%s: %d/%d/%d" % (node.name, node.discovered, node.finished, node.low)

def findArticulationPoints(gr):
   if gr.__class__ != graph.UDGraph:
      raise Exception('Incompatible graph class')
   #onFinishedCallback = lambda node: print(node.name)
   dfs = DFS(gr)
   dfs.run(printNode)


