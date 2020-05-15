import json

class Person:
    name = None
    city = None

    def __init__(self, name, city):
        Person.name = name
        Person.city = city

person1 = Person('name', 'city')
print('Person 1 name: ' + person1.name)
person2 = Person('name2', 'city2')
print('Person 1 name: ' + person1.name)
print('Person 2 name: ' + person2.name)

class Person:
    name = None
    city = None

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f'{self.name} з {self.city}'

    def __repr__(self):
        return f'{self.name} from {self.city}'
    
    def convert(self):
        return {
            'name': self.name,
            'city': self.city
        }

class SuperPerson:
    name = None
    city = None
    super_power = None

    def __init__(self, name, city, super_power):
        self.name = name
        self.city = city
        self.super_power = super_power
    
    def convert(self):
        return {
            'name': self.name
        }

mykola = Person('Mykola', 'city')
print('Person 1 name: ' + mykola.name)
fedir = Person('Пилип', 'конопель')
print('Person 1 name: ' + mykola.name)
print('Person 2 name: ' + fedir.name)
print(f'Fedir: {fedir}')
print('{fedir!r}'.format(fedir=fedir))

#name = input('Name: ')
#city = input('City: ')
#new_person = Person(name, city)

try:
    json_data = json.load(open('test.json'))
except json.decoder.JSONDecodeError:
    json_data = []

new_list = []
for item in json_data:
    new_list.append(Person(**item))
new_list.append(SuperPerson('Batman', 'Gotham', 'Money'))
print(new_list)

for item in new_list:
    if item.name == 'Fedir':
        print(item)

new_list = [person.convert() for person in new_list]

with open('test2.json', 'w+') as f:
    json.dump(new_list, f, indent=4)

# Not recommended
x = 10
def func1():
    global x
    x = 1
    print(x)

print(x)
func1()
print(x)

# Likee
x = 10
def func1(x):
    x += 1
    return x

print(x)
x = func1(x)
print(x)

#non local
x = 10 # global scope
def func2():
    global y
    print(y)
    y = 1
    x = 1 #local scope for func 2
    def closure():
        y = 10 # local scope closure
        nonlocal x
        x = 2 # local scope func2
        print(f'closure x {x}')
    print(f'local 1 x {x}')
    closure()
    print(f'local 2 x {x}')
    
y = 20
print(f'global 1 x {x}')
print(f'global 1 y {y}')
func2()
print(f'global 2 x {x}')
print(f'global 2 y {y}')


# example of using global and don't trigger teacher
global_x = 100
def first_func():
    global global_x
    global_x = 300

def second_func():
    print(global_x)

second_func()
first_func()
second_func()