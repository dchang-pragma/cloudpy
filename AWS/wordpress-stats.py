import requests
import json

# http://docs.python-requests.org/en/master/user/quickstart/#response-content

resp = requests.post('https://api.wordpress.org/themes/info/1.1/?action=query_themes&request[fields][downloaded]=true&request[fields][description]=false')
# if resp.status_code != 200:
#     # This means something went wrong.
#     raise ApiError('POST /GetPotentialAttacks2/ {}'.format(resp.status_code))
# for todo_item in resp.json():
#     print('{} {}'.format(todo_item['id'], todo_item['summary']))

#print(resp.status_code)
#resp_txt= resp.text
resp_json=resp.json()
#print (resp_txt)
print('content type: ', resp.headers['content-type'])
print('encoding: ', resp.encoding)
print(resp_json)
#print(resp.text)
#print (json.dumps(resp_json)) # convert to python object first

# resp_json has two 'objects': StatusCode and Items
print(resp_json['info']['results'])
for x in resp_json['themes']:
	print (x['name'],x['downloaded'])


# for h, f in resp_dict.items():
# 	print(h, f)


