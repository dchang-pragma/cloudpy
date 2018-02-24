graph1 = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'E'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

graph2 = {'A': set(['B', 'C', 'E']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F', 'G']),
         'D': set(['B']),
         'E': set(['A', 'B', 'D']),
         'F': set(['C']),
         'G': set(['C'])}

print(graph1)

def bfs_connected_component2(graph1, start_vertex):
	queue = [start_vertex]
	explored = []
	while queue:
		node = queue.pop(0)
		if node not in explored:
			explored.append(node)
			neighbors=graph1[node]
			# for neighbor in neighbors:
			# 	queue.append(neighbor)
			queue=queue+neighbors
	return explored

def bfs_connected_component(graph1, start_vertex):
	queue = [start_vertex]
	explored = []
	while queue:
		node = queue.pop(0)
		if node not in explored:
			explored.append(node)
			neighbors=graph1[node]
			for neighbor in neighbors:
				queue.append(neighbor)
	return explored




def dfs_iterative2(graph, start_vertex):
	'''iterative depth first search from start'''
	stack = [start_vertex]
	stackhelper = []
	explored = []
	while stack:
		node = stack.pop()
		if node not in explored:
			explored=explored+[node]
			stackhelper = graph[node]
			#print(stackhelper)
			stackhelper.reverse()
			#print(stackhelper)
			stack = stack + stackhelper
			stackhelper.reverse()
	return explored


# def bfs(graph2, start):
#     visited, queue = set(), [start]
#     while queue:
#         vertex = queue.pop(0)
#         if vertex not in visited:
#             visited.add(vertex)
#             queue.extend(graph2[vertex] - visited)
#     return visited

# print(bfs(graph2,'A'))

# def iterative_bfs(graph, start, path=[]):
#   '''iterative breadth first search from start'''
#   q=[start]
#   while q:
#     v=q.pop(0)
#     if not v in path:
#       path=path+[v]
#       q=q+graph[v]
#   return path




def dfs_iterative(graph, start):
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path


def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path


def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs(graph, start, path=[]):
  '''iterative depth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path

# reference http://www.koderdojo.com/blog/depth-first-search-in-python-recursive-and-non-recursive-programming





print('bfs_connected ', bfs_connected_component(graph1,'A'))
print('iterative bfs ', iterative_bfs(graph1, 'A'))
print('dfs_iterative2', dfs_iterative2(graph1,'A'))
print(graph1)

print('dfs_iterative*', dfs_iterative(graph1,'A'))
print('recursive dfs ', recursive_dfs(graph1, 'A'))
print('iterative dfs ', iterative_dfs(graph1, 'A'))


