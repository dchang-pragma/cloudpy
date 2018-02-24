# objects and pointers representation

# vertex
# vertex_a = vertex(1)
# vertex_b = vertex(2)
# edge = edge(vertex_a, vertex_b, 30) #


# adjacency matrix

# adjacency_matrix = [[],[]]
# adjacency_matrix[[0],[1]] = 1

w, h = 8, 5;
adjacency_matrix = [[0 for x in range(w)] for y in range(h)] 

adjacency_matrix[0][1] = 1
#adjacency_matrix[6][0] = 3 # error! range... 
adjacency_matrix[0][6] = 3 # valid

print(adjacency_matrix)
print(adjacency_matrix[0][0]) # prints 1

x, y = 0, 6 
print(adjacency_matrix[x],[y])
#print vsb[x][y] # prints 3; be careful with indexing! 

# adjacency list


no_vertex = 5;
#adjacency_list = [0 for x in range(no_vertex)] 
adjacency_list = [[],[],[],[],[]]

#print(adjacency_list)

# adjacency_list[0] = [adjacency_list[1], adjacency_list[4]] #vertex 0
# adjacency_list[1] = [adjacency_list[0], adjacency_list[2], adjacency_list[3], adjacency_list[4]] #vertex#1
# adjacency_list[2] = [adjacency_list[1], adjacency_list[3]] 
# adjacency_list[3] = [adjacency_list[1], adjacency_list[2], adjacency_list[4]] 
# adjacency_list[4] = [adjacency_list[0], adjacency_list[1], adjacency_list[3]] 
adjacency_list[0] = [1, 4] #vertex 0
adjacency_list[1] = [0, 2, 3, 4] #vertex#1
adjacency_list[2] = [1, 3] 
adjacency_list[3] = [1, 2, 4] 
adjacency_list[4] = [0, 1, 3] 

print(adjacency_list)
