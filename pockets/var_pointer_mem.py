# You’ll notice that in python, an integer object is created (in this case to represent the number 5), and subsequent variables set to that value are actually references to the same object, and thus both variables reference the same place in memory.  In C++, however, memory is allocated for the specific variable to the size of an integer, and the address in memory takes on the value 5.


def memory_address (in_var):
	return hex(id(in_var))

def func1():
	some_var = 5
	print(memory_address(some_var))

def func2():
	another_var = 5
	print(memory_address(another_var))

if __name__ == "__main__":
	int_var1 = 5
	int_var2 = 5
	print(memory_address(int_var1))
	print(memory_address(int_var2))
	print(id(int_var1))
	func1() # - meant to make variables lose their scope
	func2()


