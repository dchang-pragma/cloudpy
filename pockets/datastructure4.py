list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',] #mutable
list2 = [None]*8
dictionary1 = {1: "one", 2: "two", 3: "three"} #unordered
tuple1 = (1, 2, 3) #immutable
set1 = {1, 2, 3} #unordered; not supporting indexing; never have duplicate elements; mutable; see frozenset()



print(dictionary1[1])
print(tuple1[0])
# print(set1[2]) 
print("list1 reverse:",list1.reverse())
print("list1:", type(list1))
print("list2:", type(list2))
print("dictionary1:", type(dictionary1))
print("tuple1:", type(tuple1))
print("set1:", type(set1))

# print(list)

#print(list([1, 2, 3, 1]))
#print(dict(one = 1, two = 2, three = 3))
#print(tuple((1, 2, 3, 1)))
#print(set((1, 2, 3, 1))) # will remove duplicates

print(list1)
print(list1.index('E'))
print(len(list1))
print(dictionary1)
print(tuple1)
print(set1)

print(list1[:5]) #slicing 0 1 2 3 4
print(list1[5:]) #slicing 5 till the end