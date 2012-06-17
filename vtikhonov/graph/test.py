'''
Testing graph algorithms
'''

import graph

def testTopologicalSort():
    gr = graph.DiGraph("testTopologicalSort")
    clothes = ["shirt", "undershorts", "socks", "watch", "pants", "shoes", "belt", "tie", "jacket"]
    for item in clothes:
       gr.addNode(item)
    gr.addEdge("undershorts", "pants")
    gr.addEdge("undershorts", "shoes")
    gr.addEdge("socks", "shoes")
    gr.addEdge("pants", "belt")
    gr.addEdge("pants", "shoes")
    gr.addEdge("shirt", "belt")
    gr.addEdge("shirt", "tie")
    gr.addEdge("tie", "jacket")
    gr.addEdge("belt", "jacket")
    graph.sortTopologically(gr)
    gr.printGraph()

def testPathCounting():
   gr = graph.DiGraph("test 22.4-2")
   gr.addEdge("m", "x")
   gr.addEdge("m", "q")
   gr.addEdge("m", "r")
   gr.addEdge("n", "q")
   gr.addEdge("n", "u")
   gr.addEdge("n", "o")
   gr.addEdge("o", "r")
   gr.addEdge("o", "v")
   gr.addEdge("o", "s")
   gr.addEdge("p", "o")
   gr.addEdge("p", "s")
   gr.addEdge("p", "z")
   gr.addEdge("q", "t")
   gr.addEdge("r", "u")
   gr.addEdge("r", "y")
   gr.addEdge("s", "r")
   gr.addEdge("u", "t")
   gr.addEdge("v", "x")
   gr.addEdge("v", "w")
   gr.addEdge("w", "z")
   gr.addEdge("y", "v")
   print graph.countPaths(gr, "p", "v")
   #gr.printGraph()

if __name__=="__main__":
   #testTopologicalSort()
   testPathCounting()

