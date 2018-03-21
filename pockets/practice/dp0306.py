graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

print(graph['A'])

for k, v in graph.items():
	print(k, v)

for j in graph.keys():
	print(j)

for i in graph.values():
	print(i)

graph_iters = iter(graph)


#print(graph_iters.next())
print(next(graph_iters))
print(next(graph_iters))
# print(next(iter(graph)))