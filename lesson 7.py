from package1 import calculations


from package1.module1 import _b
from package1.package2.module2 import *
result = calculations.sum(1, 2)
print(result)
print(calculations)
print(b)

print(_b)

import lesson7_add
print(lesson7_add.validate('1', '2'))

from lesson7_add import validate
print(validate('1', '2'))

import lesson7_add
print(lesson7_add.validate('1', '2'))

from package1.calculations import sum, div
result = sum(1, 2)
print(f'Result: {result}')

from package1.package2.module2 import b
print(f'B from module 2: {b}')

from package1 import module1 
from package3 import module1
a = 1
a = 10
print(f'p: {module1.a}')

from package1 import module1 as p1m1
from package3 import module1 as p3m1

print(f'p1: {p1m1.a}')
print(f'p3: {p3m1.a}')