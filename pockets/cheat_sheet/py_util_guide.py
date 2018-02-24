import os, subprocess, shutil
# commands was replaced by subprocess in python3 https://docs.python.org/3/library/subprocess.html#module-subprocess
def printdir(dir):
	filenames = os.listdir(dir)
	#os.mkdir('./testByPython')

	for filename in filenames:
		print(filename)  ## foo.txt
		#print(os.path.join(dir, filename)) ## dir/foo.txt (relative to current dir)
		#print(os.path.abspath(os.path.join(dir, filename))) ## /home/nick/dir/foo.txt


printdir('./')


def list_file(path, file_type):
    file_list = []
    with os.scandir(path) as dir_content:
        for line in dir_content:
            if line.name.endswith('.'+file_type) and line.is_file():
                file_list.append(line.name)
    return file_list

#file_list = list_file('.','html')
#first_file_name = file_list[0]


def copy_file(source, destination):
	shutil.copy(source, destination)



#copy_file('./small.txt','./small2.txt')

#subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)

local_dir = './test_2'
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

