'''
Testing graph algorithms
'''

import graph

if __name__=="__main__":
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
    #gr.nodes.sort()
    graph.sortTopologically(gr)
    gr.printGraph()
