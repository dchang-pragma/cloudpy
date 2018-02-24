#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
# added by bunmaster
import subprocess
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

# def printdir(dir):
#   filenames = os.listdir(dir)
#   #os.mkdir('./testByPython')

#   for filename in filenames:
#     print(filename)  ## foo.txt
#     #print(os.path.join(dir, filename)) ## dir/foo.txt (relative to current dir)
#     #print(os.path.abspath(os.path.join(dir, filename))) ## /home/nick/dir/foo.txt


# printdir('./')

def sort_by_name(name_rank_tuple):
  return name_rank_tuple[0]

def list_file(path, file_type):
  file_list = []
  with os.scandir(path) as dir_content:
    for line in dir_content:
      if line.name.endswith('.'+file_type) and line.is_file():
        file_list.append(line.name)
  return file_list

#file_list = list_file('.','html')
#first_file_name = file_list[0]

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename, 'rU')
  str_content = f.read()
  f.close()
  match1 = (re.search('<h3.*>', str_content)) # find the year line
  match_year = (re.search('\d\d\d\d', match1.group()))
  match3 = re.findall(r'<tr align="right"><td>.*>',str_content)
  dict2004 = {}
  list2004 = []
  for str_rank in match3:
    match_name = re.search('(\d+)</td><td>([\w]+)</td><td>([\w]+)', str_rank)
  #dict2004[match_name.group(1)] = (match_name.group(2),match_name.group(3))
    list2004.append((match_name.group(2), match_name.group(1)))
    list2004.append((match_name.group(3), match_name.group(1)))
  list2004_sorted = sorted(list2004, key=sort_by_name, reverse=False)

  #print(str_content)
  # +++your code here+++

  return list2004_sorted



#print(dict2004)




#print('match3',len(match3))
#print(match2.group())
#match_rank = re.search('\d+', match2.group())
#match_name = re.search('</td><td>\w+', match2.group())
#match_name = re.search('(\d+)</td><td>([\w]+)</td><td>([\w]+)', match2.group())
#match = (re.search('\d\d\d\d', str_content))
#print(type(match1))
#print(match_year.group())
#print(match_rank.group())
#print(match_name.group(1))
# print(match2)





def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)


  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    if summary:
      list_name_rank = extract_names(args[0])
      outf = open(args[0]+'.summary', 'w')
      for str_rank in list_name_rank:
        outf.write(str_rank[0]+' '+str_rank[1]+'\n')
    outf.close()


  else:
    list_name_rank = extract_names(args[0])
    for str_rank in list_name_rank:
      print(str_rank[0], ' ', str_rank[1])    
    # print('\n'.join(list_name_rank) + '\n')

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
