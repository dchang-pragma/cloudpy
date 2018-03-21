strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']
nums = [(1,3),(2,4),(7,8,1)]

def last(a):
	return a[-1]

print(sorted(nums,key=last))



(x, y, z) = (42, 13, "hike")
print(z)  ## hike
(err_string, err_code) = Foo('error', 500)  ## Foo() returns a length-2 tuple
