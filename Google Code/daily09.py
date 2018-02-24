import os, subprocess
# commands was replaced by subprocess in python3 https://docs.python.org/3/library/subprocess.html#module-subprocess
def printdir(dir):
	filenames = os.listdir(dir)
	#os.mkdir('./testByPython')

	for filename in filenames:
		print(filename)  ## foo.txt
		print(os.path.join(dir, filename)) ## dir/foo.txt (relative to current dir)
		print(os.path.abspath(os.path.join(dir, filename))) ## /home/nick/dir/foo.txt


#printdir('./')


def listdir(dir):
    cmd = 'ls -l ' + dir
    print("Command to run:", cmd)   ## good to debug cmd before actually running it
    (status, output) = subprocess.getstatusoutput(cmd)
    if status:    ## Error case, print the command's output to stderr and exit
        sys.stderr.write(output)
        sys.exit(status)
    print(output)  ## Otherwise do something with the command's output


listdir('./')