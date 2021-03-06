'''
Testing graph algorithms
'''

import graph, algorithm

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
    algorithm.sortTopologically(gr)
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
   print algorithm.countPaths(gr, "p", "v")
   #gr.printGraph()

def testArticulationPoints():
   gr = graph.UDGraph("Articulation_Points")
   gr.addEdge("1", "6")
   gr.addEdge("1", "7")
   gr.addEdge("1", "15")
   #gr.addEdge("1", "33")
   gr.addEdge("2", "3")
   gr.addEdge("2", "8")
   gr.addEdge("3", "8")
   gr.addEdge("4", "9")
   gr.addEdge("4", "10")
   gr.addEdge("5", "13")
   gr.addEdge("5", "14")
   gr.addEdge("5", "20")
   gr.addEdge("6", "7")
   gr.addEdge("6", "15")
   gr.addEdge("7", "8")
   gr.addEdge("7", "15")
   gr.addEdge("8", "9")
   gr.addEdge("8", "16")
   gr.addEdge("8", "17")
   gr.addEdge("9", "18")
   gr.addEdge("10", "11")
   gr.addEdge("10", "18")
   gr.addEdge("11", "13")
   gr.addEdge("11", "20")
   gr.addEdge("13", "14")
   gr.addEdge("13", "20")
   gr.addEdge("16", "17")
   gr.addEdge("16", "21")
   gr.addEdge("19", "22")
   gr.addEdge("19", "23")
   gr.addEdge("20", "23")
   gr.addEdge("20", "24")
   gr.addEdge("22", "23")
   algorithm.findArticulationPoints(gr)

if __name__=="__main__":
   #testTopologicalSort()
   #testPathCounting()
   testArticulationPoints()

