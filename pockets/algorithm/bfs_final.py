graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs_connected_component(graph, start):
    explored = [] # keep tracked of explored node
    queue = [start] # implement queue as list
    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
 
print('bfs A', bfs_connected_component(graph,'A')) # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']