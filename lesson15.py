from copy import deepcopy

def get_sqr(numbers_list):
    for item in numbers_list:
        if type(item) != int and type(item) != float:
            raise ValueError
    intermid_list = []
    for item in numbers_list:
        intermid_list.append(item**2)
    return intermid_list

example = [1,2,3,4]

print(get_sqr(example))

def get_sqr_2(numbers_list):
    if any(type(item) != int and type(item) != float for item in numbers_list):
        raise ValueError
    intermid_list = [item**2 for item in numbers_list]
    return intermid_list

example = [1,2,3,4]

print(get_sqr(example))
print(get_sqr_2(example))


def own_any(iterable):
    for item in iterable:
        if item: # if item True, If item >= 1, If len(item) >=1, if item is not None ...
            return

own_any(['', [], {}, 0, '123', ''])

def read_file():
    index = 10
    with open('test.json') as f:
        for i in f:
            print('First step')
            index += 1
            print(index)
            yield i
            print('second step')

file_data = read_file()
print(file_data)
#Function's not been called

print('Get first line')
print(next(file_data)) # first line
print()
print('Get second line')
print(next(file_data)) # second line
print()
print('Get third line')
print(next(file_data)) # third line
print()

def fib():
    num = 1
    next_num = 1
    while True:
        yield num
        yield num
        yield num
        yield num
        num, next_num = next_num, num + next_num
"""
Danger zone:
DO NOT UNCOMMENT
with open('fib', 'w') as f:
    for fib_num in fib():
        f.write(str(fib_num))
        f.write('\n')
"""

first = fib()
second = fib()

print('FIRST')
for item in first:
    print(item)
    if item % 5 == 0:
        break

print('SECOND')
for item in second:
    print(item)
    if item > 1000:
        break

class Person:
    def __init__(self, name, phone):
        self.name = name
        if type(phone) != str or not phone.isdigit():
            raise ValueError(f'{phone} should contain numbers only')
        self.phone = phone

    def __str__(self):
        return f'{self.name}: {self.phone}'

    def __repr__(self):
        return f'{self.name}: {self.phone}'

class PhoneBook:
    def __init__(self, *args):
        if any(not isinstance(person, Person) for person in args):
            raise ValueError
        self.ppl1 = list(args)
        self.ppl2 = list(args)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.ppl1):
            raise StopIteration
        person = self.ppl1[self.index],  self.ppl2[self.index]
        self.index += 1
        return person


class list2:
    def __init__(self, *args):
        self.args = args
        self.index = 0
 
    def __iter__(self):
        # will be called by for loop or using method iter()
        self.index = 0 # Reset counter to start from the begin in each "for" loop 
        return self

    def __next__(self):
        # will be called by for loop or using method next()
        if self.index >= len(self.args):
            raise StopIteration
        value = self.args[self.index]
        self.index += 1
        return value

new_list = list2(1,2,3,4,5)

for i in new_list:
    print(i)

for i in new_list:
    print(i)

person1 = Person('Спок', '044123454')
person2 = Person('Енакін', '0362123454')
person3 = Person('Ашот', '057123454')
person4 = Person('Рафік', '0536123454')
person5 = Person('Смеагорн', '0566123454')

phonebook = PhoneBook(person1, person2, person3, person4, person5)
print(next(phonebook))
print(next(phonebook))

for person in phonebook:
    print(person)




class PhoneBookDict:
    def __init__(self, *args):
        if any(not isinstance(person, Person) for person in args):
            raise ValueError
        self.ppl = {
            person.phone: person.name for person in args
        }
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.ppl):
            raise StopIteration
        phone = list(self.ppl)[self.index]
        self.index += 1
        return self.ppl[phone]

phonebook = PhoneBookDict(person1, person2, person3, person4, person5)
for person in phonebook:
    print(person)