import urllib.request, urllib.parse # In Python 3, urllib and urllib2 are merged into urllib.request, and urlparse becomes urllib.parse. All of their exceptions are in urllib.error.
#import urllib.parse

def wget(url):
    ufile = urllib.request.urlopen(url)  ## get file-like object for url
    info = ufile.info()   ## meta-info about the url content
    # if info.gettype() == 'text/html':
    # 	print('base url:' + ufile.geturl())
    # 	text = ufile.read()  ## read all its text
    # 	print(text)

    print(ufile)
    print(info)



#wget('http://www.stayfocusd.com/')

url = 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baai.jpg'

url_split_result = urllib.parse.urlsplit(url)
print(type(url_split_result))
print(url_split_result)
#local_file_name = url_split_result.path.split("/")[-1]
local_file_name = '/tmp/' + url_split_result.path.split("/")[-1]

print(local_file_name)

#urllib.urlretrieve(url, filename)


local_file = urllib.request.urlretrieve(url,local_file_name)
print(local_file)
print(type(local_file)) # tuple


# local_filename, headers = urllib.request.urlretrieve('http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baai.jpg')
# html = open(local_filename)