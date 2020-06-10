import os
import glob

import itertools

class IterableSimple:
    def __init__(self, iterable):
        self.__iter = iterable
    
    def __iter__(self):
        return iter(self.__iter)
    
    def __getitem__(self, index):
        return self.__iter[index]



simple = IterableSimple([1,2,3,4,5,6])
print(simple[2])
for item in simple:
    print(item)


class IterableSimple1:
    def __init__(self, item1, item2, item3):
        self.__item1 = item1
        self.__item2 = item2
        self.__item3 = item3
        self.__index = 0
    
    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        self.__index += 1
        if self.__index > 3:
            raise StopIteration
        if self.__index == 1:
            return self.__item1
        elif self.__index == 2:
            return self.__item2
        elif self.__index == 3:
            return self.__item3
        else:
            raise StopIteration
print('Hellish iterator')
customIter = IterableSimple1(1,2,3)
for item in customIter:
    print(item)


class IterableSimple2:
    def __init__(self, item1, item2, item3):
        self.__item1 = item1
        self.__item2 = item2
        self.__item3 = item3
    
    def __iter__(self):
        return iter([self.__item1, self.__item2, self.__item3])

print('Hellish iterator 2')
customIter = IterableSimple2(1,2,3)
for item in customIter:
    print(item)

class NonIterableIterator:
    def __init__(self, item1, item2, item3):
        self.__item1 = item1
        self.__item2 = item2
        self.__item3 = item3
        self.__index = 0
    
    def __next__(self):
        self.__index += 1
        if self.__index > 3:
            raise StopIteration
        if self.__index == 1:
            return self.__item1
        elif self.__index == 2:
            return self.__item2
        elif self.__index == 3:
            return self.__item3
        else:
            raise StopIteration

print('Hellish iterator 3')
customIter = NonIterableIterator(1,2,3)
print(next(customIter))

print(range(10))
print(list(range(10)))

def generator_range():
    index = 0
    while True:
        print(index)
        yield index
        index += 1

print(any(item == 3 for item in generator_range()))
print(all(item == 0 for item in generator_range()))

keys = ['1', '2', '3', '4', '5', '7', '10']
values = [1, 2, 3, 4, 5]
dict_simple = dict((('1', 1), ('2', 2)))
print(dict_simple)

zipped = zip(keys, values)
print(list(zipped))

print(list(itertools.zip_longest(keys, values, fillvalue='шашличок')))

def div_to_2(item):
    return item % 3 == 0


print(filter(lambda item: item % 2 == 0, range(10)))
print(list(filter(lambda item: item % 2 == 0, range(10))))
print(list(filter(div_to_2, range(10))))


def all_2(item):
    return item

print(map(lambda item: item**2, range(10)))
print(list(map(lambda item: item**2, range(10))))
print(list(map(all_2, IterableSimple2(1,2,3))))

print(os.getcwd())
for root, dirs, files in os.walk(os.getcwd()):
    print(root, dirs, files)
os.chdir('D:\git')

print('Current dir')
print(os.getcwd())
print('Dirs')
print(os.listdir(os.getcwd()))
os.chdir('D:\git\Python-test-repo-phase-1')
print('Glob pattern all files name starts from lesson1')
print(glob.glob('lesson1*.py'))
print('Glob pattern all files name starts from lesson1 and ends with .py')
print(glob.glob('lesson??.py'))

print(glob.glob('*esso*.py'))
print(glob.glob('????????.py'))


#print(os.unlink('test.py'))
print(os.system(f'dir {os.getcwd()}'))

