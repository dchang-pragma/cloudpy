#words = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
#words = ['bbb', 'ccc', 'xaa', 'xzz', 'axx']
words = ['xaa', 'xzz', 'bbb', 'ccc', 'axx']
#words = ['xaa', 'bbb', 'xzz', 'ccc', 'axx']
x_words = []
#print(words)
#other_words = []
# for word in words:
#   if word.startswith('x'):
#     #print(words)
#     x_words.append(word)
#     words.remove(word)
#   #print(x_words)
# # +++your code here+++
#   print(len(words))
# #return sorted(x_words)+sorted(other_words)
# print(sorted(x_words)+sorted(words))


x_count=0
for word in words:
  print('words before', words)
  if word.startswith('x'):
    x_count = x_count+1
    
    x_words.append(word)
    #print(words)
    words.remove(word)
    
  print('words after ', words)
  print(word)
#print(x_count)
#print(x_words)
#print(words)
print(sorted(x_words), sorted(words))
