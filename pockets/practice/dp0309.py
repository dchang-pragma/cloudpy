def all_subsets(given_array):
	subset = [None] * len(given_array)
	helper(given_array, subset, 0)


def helper(given_array, subset, i):
	if i == len(given_array):
		print(subset)
	else:
		subset[i] = None
		helper(given_array, subset, i+1)
		subset[i] = given_array[i] # using list is easier to track than set
		helper(given_array, subset, i+1)



given_array = [1, 2, 3, 4, 5]

all_subsets(given_array)




