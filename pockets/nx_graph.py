import networkx as nx

g=nx.Graph()
#print(type(g))
g.add_node(1)
g.add_nodes_from([2,3])

g.add_edge(1,2)
g.add_edge(1,5)

print(g.number_of_nodes())
print(g.number_of_edges())
print(type(g.neighbors(1)))