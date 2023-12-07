import networkx as nx

graph_data = nx.DiGraph({
    ("A", "B"): 1,
    ("A", "C"): 2,
    ("B", "C"): 3,
})
graph = nx.DiGraph(graph_data)
nodes = graph.nodes()
edges = graph.edges()

print("Nodes:", nodes)
print("Edges:", edges)
