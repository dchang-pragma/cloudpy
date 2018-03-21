given_array = [1, 2, 3]

def add_one(given_array):
	carry = 1
	result = [None] * len(given_array)
	#print(result)
	for i in range(len(given_array)-1, -1, -1):
		total = given_array[i] + carry
		if total == 10:
			carry = 1
		else:
			carry = 0
			result[i] = total%10
	if carry ==1:
		result = [None] * (len(given_array)+1)
		result[0] = 1
	return result




after_array = add_one(given_array)
print(after_array)





# for j in range(2, -1, -1):
for j in range(2, -1, -1):
	print(j)
