import json

readme_file = open('README.md')
print(readme_file.tell())
print(readme_file.read(9))
print(readme_file.tell())
print(readme_file.read(9))
print(readme_file.tell())
readme_file.seek(0)
print(readme_file.read(9))

print(dir(readme_file))

readme_file.seek(0)
print('The first line: ' + readme_file.readline())
print(readme_file.tell())
print('The second line: ' + readme_file.readline())
print(readme_file.tell())
print('The third line: ' + readme_file.readline())

readme_file.seek(0)
print(readme_file.readlines()[2])
print('read in loop')
readme_file.seek(0)

elem = 'a'
count = 0
for item in readme_file:
    if item == elem:
        count += 1
    if count >= 1:
        break
    print(item)


new_file = open('new_file', 'w')
new_file.write('123')
new_file.write('\n')
new_file.close()

new_file = open('new_file', 'a')
new_file.write('12sda3')
new_file.close()


print('NEW')
new_file = open('new_file2', 'r+')
new_file.write('abcdefg')
print(f'Cursor: Symbol #{new_file.tell()}')
new_file.write('\nabcdefg')
print(f'Cursor: Symbol #{new_file.tell()}')
new_file.seek(1)
new_file.write('456')
print(f'Cursor: Symbol after write #{new_file.tell()}')
print(new_file.read(3))
print(f'Cursor: Symbol after read #{new_file.tell()}')
new_file.write('456')
print(f'Cursor: Symbol after write #{new_file.tell()}')
new_file.close()

print('NEW')
new_file = open('new_file2', 'w+')
new_file.write('abcdefg')
print(f'Cursor: Symbol #{new_file.tell()}')
new_file.write('\nabcdefg')
print(f'Cursor: Symbol #{new_file.tell()}')
new_file.seek(1)
new_file.write('456')
print(f'Cursor: Symbol after write #{new_file.tell()}')
print(new_file.read(3))
print(f'Cursor: Symbol after read #{new_file.tell()}')
new_file.write('456')
print(f'Cursor: Symbol after write #{new_file.tell()}')
new_file.close()


new_file = open('new_file2', 'a+')
new_file.seek(88888)
new_file.write('12sda3')
new_file.read(3)
new_file.close()

g = 801123459
g1 = str(g)
whole = len(g1) // 2
modulus = len(g1) % 2
print(whole)
for i in range(1, (whole) + 1):
    if i == 1:
        print(int(g1[-2*i:]))
    elif i == 2:
        print(int(g1[-2*i:-i]))
    else:
        print(int(g1[-2*i:-2*(i-1)]))
if modulus:
    print(int(g1[:modulus]))


#JSON 
json_like = [{
    'name': 'Sasha',
    'magazines': ['Куншт', 'ШО']
}, {
    'name': 'Bogdan',
    'magazines': ['Maxim', 'Бабушкина грядка', 'Нашали', 'Mens Health']
}]

#Lookup map
dict_like1 = {
    'Sasha': ['Куншт', 'ШО'],
    'Bogdan': ['Maxim', 'Бабушкина грядка', 'Нашали', 'Mens Health']
}

dict_like2 = {
    'Sasha': {
        'magazines': ['Куншт', 'ШО']
    },
    'Bogdan': {
        'magazines': ['Maxim', 'Бабушкина грядка', 'Нашали', 'Mens Health']
    }
}

#JSON 
json_like = [{
    'operation': '+',
    'description': 'Plus',
    'function': 'sum',
    'характер': 'Нордический',
    'arguments_count': 2
}, {
    'operation': '-',
    'характер': 'Нордический',
    'description': 'sub',
    'function': 'lambda a, b: a - b',
    'arguments_count': 2
}]

#JSON 
json_like_map = {
'+': {
    'operation': '+',
    'description': 'Plus',
    'function': 'sum',
    'характер': 'Нордический',
    'arguments_count': 2
}, 
'-': {
    'operation': '-',
    'характер': 'Нордический',
    'description': 'sub',
    'function': 'lambda a, b: a - b',
    'arguments_count': 2
}}

operations = {
    '+': 'Plus',
    '-': 'sub'
}

operations_funcs = {
    '+': sum,
    '-': lambda a, b: a - b
}


# How to search in dict lookup map
query = '+'
if query in operations_funcs:
    print('+')

# How to search in json
query = '+'
for item in json_like:
    if query == item['operation']:
        print(item)
        break

for item in json_like:
    print(f"Name: {item['operation']}")
    print(f"Description: {item['description']}")
    print(f"Характер: {item['характер']}")

print(dict_like2)

json_file = open('new2.json', 'w')
print('Simple print')
print(json_like)
print('Json print')
print(json.dumps(json_like, indent=4))
json.dump(json_like, json_file, indent=4)
json_file.close()

json_file = open('new.json', 'r')
print('Simple print')
json_content = ''.join([i for i in json_file])
print(json_content)
json_object = json.loads(json_content)
print(type(json_object))

json_file.seek(0)
print('Json print')
print(json.load(json_file))



example = json.loads('[{"name": "Sasha"}]')
print(example[0]['name'])


with open('new.json', 'a') as json_file:
    print(json_file.write('10'))

print('Папа')