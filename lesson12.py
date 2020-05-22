class Number:
    def __init__(self, a):
        self.a = a
    
    def division(self, b):
        print('Simple number division')
        if b != 0:
            return self.a / b
        raise ZeroDivisionError('Cannot divide by zero')

class Integer(Number):
    def division(self, b):
        print('Integer division')
        result = super().division(b)
        return int(result)

number_two = Number(1)
print(number_two.division(2))

integer_ten = Integer(10)
print(integer_ten.division(3))

print(Integer.mro())
print(Number.__dict__)
print(Integer.__dict__)
print(integer_ten.__dict__)


print(isinstance(integer_ten, Integer))
print(isinstance(integer_ten, Number))


if isinstance(number_two, Number):
    print('This is number')
elif isinstance(number_two, Integer):
    print('This is integer')

print(issubclass(Integer, Number))
print(issubclass(Number, Integer))

class CaseError(Exception):
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        print('Увага, зараз буде Стрічка')
        return ''.join(self.args)

    def __repr__(self):
        return ''.join(self.args)

error = CaseError(f'A should be lower or capitalized')
if isinstance(error, Exception):
    print('Exception')
elif isinstance(error, CaseError):
    print('CaseError')

try:
    name = 'AAAAAAA'
    if name.isupper():
        raise CaseError(f'{name} should be lower or capitalized', 'Or smth like this')
except CaseError as e:
    print(type(e))
    print(dir(e))
    print(str(e))
    print(repr(e))
    print(e.args[0])

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __add__(self, other):
        return self.age + other.age

    def __pow__(self, other):
        return self.age ** other.age

    def __pos__(self):
        self.age += 1 

first_kid = Person('Jim', 10)
first_again_kid = Person('Jim', 10)
second_kid = Person('Cat', 5)

if first_kid.__eq__(first_again_kid):
    print('Same kid')



if second_kid < first_kid:
    print('First kid is an older')

if second_kid <= first_kid:
    print('First kid is an older or equal')

if first_kid < first_again_kid:
    print('first again kid is an older')

if first_kid <= first_again_kid:
    print('first again kid is an older or eqaul')

print(first_kid + second_kid)
# /\ Equal to \/
print(first_kid.__add__(second_kid))

print(first_kid ** second_kid)

print(second_kid.age)
+second_kid
print(second_kid.age)
# A + B + C
# T = A + B
# T + C

class Number:
    def __init__(self, a):
        self.a = a
    
    def __add__(self, other):
        result = self.a + other.a
        return Number(result)
 
    def __str__(self):
        return str(self.a)
        
    def __int__(self):
        return int(self.a)

print('1 + 2 + 4')
print(((Number(1) + Number(2)) + Number(4)) + Number(5))
new_number = Number(1) + Number(2)
new_number = new_number + Number(4)
new_number = new_number + Number(5)


print(int(Number(5)))

class LNumber:
    def __init__(self, a):
        self.a = a
 
    def __str__(self):
        return str(self.a)

class RNumber:
    def __init__(self, a):
        self.a = a
    
    def __radd__(self, other):
        result = self.a + other.a
        return Number(result)
 
    def __str__(self):
        return str(self.a)

print(LNumber(5) + RNumber(5))



class Extra:
    def __init__(self, a):
        self.__a = a
        self.__private()

    def getA(self):
        return self.__a

    def setA(self, a):
        self.__a = a
    
    def __private(self):
        print('I\'m private')
        print('You WIN! Возми на полке пирожок!')
    
    def _semi_private(self):
        print('I\'m protected')
        print('You WIN! Возми на полке пирожок!')


extra = Extra(5)
print(extra.getA())
extra._semi_private()
