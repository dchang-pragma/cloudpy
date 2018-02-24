import os
# with os.scandir('.') as it:
# 	for entry in it:
# 		if not entry.name.endswith('.txt') and entry.is_file():
# 			print(entry.name)

# It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running

#dir_content = os.scandir('.')
with os.scandir('.') as dir_content:
	print(type(dir_content))
	for line in dir_content:
		if line.name.endswith('.py') and line.is_file():
			print(line.name)
	print(type(line))