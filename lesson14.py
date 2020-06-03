import time
from functools import wraps

class Example:
    def __init__(self, msg=''):
        self.msg = msg

    def __call__(self, abc='abc'):
        return abc


example = Example('msd')
print(example.msg)
print(example(3232))



def check_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Doc string for decorator"""
        t1 = time.time()
        return_value = func(*args, **kwargs)
        t2 = time.time()
        print(f'Executed in {t2-t1}')
        return return_value
    return wrapper

class Decorator:
    def __init__(self, func):
        self.func = func

    def smth(self):
        print('You are not supposed to be here')

    def __call__(self, *args, **kwargs):
        self.time1 = time.time()
        return_value = self.func(*args, **kwargs)
        t2 = time.time()
        print(f'Executed in {t2-self.time1}')
        return return_value

@Decorator
def print_value(value):
    print(value)

print_value('123')

# Що насправді те саме що і \/
#1. print_value = Decorator(print_value)
#print_value('Print me softly')

def decorator_method(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print('Call wrapper function')
        print(help(func))
        print('With self:')
        print(self)
        print('With args:')
        print(args)
        print('With kwargs')
        print(kwargs)
        return func(self, *args, **kwargs)
    return wrapper

class Unperfect:
    def __init__(self, numbers):
        if type(numbers) == list:
            self.numbers = numbers
        else:
            raise ValueError

    @decorator_method
    def make_perfect(self):
        return sorted(self.numbers)

    def __str__(self):
        return f"unperfect list: {','.join([str(i) for i in self.numbers])}"

    def __repr__(self):
        return f"unperfect list: {','.join([str(i) for i in self.numbers])}"

unperfect = Unperfect([1,7,4,3,7,3,0])
print(unperfect.make_perfect())


class X:
    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if type(x) != int and type(x) != float:
            raise ValueError(f'{x} must be a number')
        self.__x = x

class_x = X(5)
print(class_x.get_x())
class_x.set_x(10)
print(class_x.get_x())

class XWithPower:
    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if type(x) != int and type(x) != float:
            raise ValueError(f'{x} must be a number')
        self.__x = x

    x = property(get_x, set_x)

class_x = XWithPower(5)
print(class_x.x)
class_x.x = 8
print(class_x.x)

class Student:
    def __init__(self, name, city):
        self.__name = name
        self.__city = city

    def getName(self):
        return self.__name
    
    def setName(self, name):
        if type(name) != str or not name.isalpha():
            raise ValueError('Wrong name')
        self.__name = name
    
    name = property(getName, setName)

    def getCity(self):
        return self.__city
    
    def setCity(self, city):
        if city not in ['City17', 'Rivne', 'Bravos', 'Zone51']:
            raise ValueError('Wrong city.')
        self.__city = city
    
    city = property(getCity, setCity)

student = Student('Name', 'City')
# Option 1
student.setCity('Zone51')

# Option 2 with properties
student.city = 'Zone51'
print(student.city)

class Student:
    def __init__(self, name, city):
        self.__name = name
        self.__city = city

    @property
    def name(self):
        return self.__name


student = Student('Name', 'City')
print(student.name)

## Read about @staticmethod and @classmethod