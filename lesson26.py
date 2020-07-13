Str = 'asvbfdgfdfg' # == ['a', 's', 'v' ....'ф', 'п']
Bytes = b'abfd'
Encoded = bytes('asdasd', encoding='utf-8')
bytes_to_Str = Encoded.decode('utf-8')

for i in 'abcd':
    print(i)
print('')
print('')
for i in b'abcd':
    print(chr(i))
print('')
print('')
for i in Encoded:
    print(chr(i))
print('')
print('')
for i in bytes_to_Str:
    print(i)
print('')
print('')

with open('hhh2.txt', 'wb') as f:
    f.write(Encoded)

hello = open('hhh.jpg', 'rb').read()

with open('hhh2.jpg', 'wb') as f:
    f.write(hello)

import requests

resource = requests.get('https://xkcd.com/1987/')

print(resource.text)

resource = requests.get('https://imgs.xkcd.com/comics/python_environment.png')
with open('python.png', 'wb') as f:
    f.write(resource.content)


resource = requests.get('https://httpbin.org/get', params={'things': 2})
print(resource.text)


resource = requests.get('https://api.github.com/search/repositories', params={'q': 'anime:javascript'})
print(type(resource.json()))
for item in resource.json()['items']:
    print(item['owner'])
    print(item['name'])
    print(item['html_url'])
