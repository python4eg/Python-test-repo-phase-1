import os
from contextlib import contextmanager

with open('test.json') as f:
    print(f.read())


class File:
    def __init__(self, file_name):
        if os.path.exists(file_name):
            self.__file = open(file_name)
        else:
            raise ValueError(f'{file_name} does not exist')
    
    def __enter__(self):
        print('Create context')
        return self.__file
    
    def __exit__(self, type, value, traceback):
        print('Leaving context and close file')
        self.__file.close()


with File('test.json') as f1:
    print(f1.read())


class TempMutableList:
    def __init__(self, data):
        self.list = data
        self.__local_list = data[:]
    
    def __enter__(self):
        return self.list
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.list = self.__local_list[:]

tempData = TempMutableList([1,2,3,4])
print(tempData.list)
with tempData as l1:
    l1.append(5)
    print(l1)
    print(tempData.list)
print(tempData.list)

@contextmanager
def file_example(file_name):
    file_obj = open(file_name)
    yield file_obj
    print('Trying to close')
    file_obj.close()

with file_example('test.json') as f1:
    print(f1.read())

@contextmanager
def file_example_raise(file_name):
    file_obj = open(file_name)
    try:
        yield file_obj
    finally:
        print('Trying to close')
        file_obj.close()


try:
    with file_example_raise('test.json') as f1:
        raise ValueError
        print(f1.read())
except:
    pass

import package1
print(package1.f)