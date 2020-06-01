class Product:
    def __init__(self, p_name, p_type):
        try:
            if type(p_name) != str:
                raise ValueError('Name should be string.')
            self.p_name = p_name
            self.p_type = p_type
        except ValueError as e:
            self.p_name = 'Dummy product'
            self.p_type = 'Dummy type'
    
    def __str__(self):
        return f'Cool product {self.p_name}'
    
    def __repr__(self):
        return f'Cool product {self.p_name}'

class ProductGoodExample:
    def __init__(self, p_name, p_type):
        if type(p_name) != str:
            raise ValueError('Name should be string.')
        self.p_name = p_name
        self.p_type = p_type
    
    def __str__(self):
        return f'Cool product {self.p_name}'
    
    def __repr__(self):
        return f'Cool product {self.p_name}'

class ProductStore:
    def __init__(self, product):
        self.storage = [{
            'product': product,
            'amount': 0
        }]
    
    def set_discount_wrong(self, identifier, discount):
        for item in storage:
            product = item['product']
            if product.p_type == id_name or product.p_name == id_name:
                print(product)
    
    def set_discount_chiotko(self, identifier, identifier_name, discount):
        for item in storage:
            product = item['product']
            if identifier == 'type':
                if product.p_type == id_name or product.p_name == id_name:
                    print(product)
            elif identifier == 'name':
                if pproduct.p_name == id_name:
                    print(product)
items = []
try:
    p1 = Product("Orange", "Apples")
    print(p1)
    items.append(p1)
    p2 = ProductGoodExample(1, 2)
    print(p2)
    
    items.append(p2)
except ValueError as e:
    print(e)

print(items)

import time
from functools import wraps


def check_time(func):
    def wrapper(*args, **kwargs):
        """Doc string for decorator"""
        t1 = time.time()
        return_value = func(*args, **kwargs)
        t2 = time.time()
        print(f'Executed in {t2-t1}')
        return 1, return_value
    return wrapper

@check_time
def calculate(x1, x2):
    "Take x1 power to x2"
    return x1 ** x2

@check_time
def add(x1, x2, x3):
    return x1 + x2 + x3

# ____
# @check_time <==> calculate = check_time(calculate)

r = calculate(1000, 100)

def example(x1, x2):
    """Doc string for example"""
    pass

print(help(example))
print(example.__name__)
print(example.__doc__)

print(help(calculate))
print(calculate.__name__)
print(calculate.__doc__)

import inspect
print(inspect.signature(calculate))



def conditional_time(func):
    @wraps(func)
    def wrapper(*args, time_it=True, **kwargs):
        print(args)
        print(kwargs)
        if time_it:
            t1 = time.time()
            return_value = func()
            t2 = time.time()
            print(f'Executed in {t2-t1}')
            return return_value
        return func()
    return wrapper

@conditional_time
def uppercut():
    value = input('Give your value: ')
    return value.upper()

print('With time')
print(uppercut())

print('Without time')
print(uppercut(1, time_it=False, x1=1))

open('logfile.log', 'w').close()


def check_time_file_name(filename):
    print("2. Створюємо функцію check_time")
    def check_time(func):
        print(f"4. Заміняємо функцію {func.__name__} функцією wrapper")
        def wrapper(*args, **kwargs):
            print(f'7. Виконуємо функцію wrapper як функцію {func.__name__}')
            """Doc string for decorator"""
            t1 = time.time()
            return_value = func(*args, **kwargs)
            t2 = time.time()
            with open(filename, 'a') as logger:
                logger.write(f'{func.__name__} executed in {t2-t1}')
                logger.write('\n')
            print(f'9. Повертаємо результат виконання функції {func.__name__}')
            return return_value
        print(f"5. Повертаємо функцію wrapper")
        return wrapper
    print("3. Повертаємо функцію check_time")
    return check_time
    
print("1. Оголошення функції і декоратора")
@check_time_file_name('logfile.log')
def reverse(list_to_reorder):
    print('8. Виконуємо функцію reverse')
    return list_to_reorder[::-1]

print('6. Виконання функції')
print(reverse([1,2]))
"""
@check_time_file_name('logfile.log')
def reverse(list_to_reorder):
    return list_to_reorder[::-1]

\/
reverse = check_time_file_name('logtime')(reverse)

\/
check_time = check_time_file_name('logtime')
reverse = check_time(reverse)



check_time = check_time_file_name('logfile.log')
print(check_time)

def check_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        return_value = func(*args, **kwargs)
        t2 = time.time()
        with open('logfile.log', 'a') as logger:
            logger.write(f'{func.__name__} executed in {t2-t1}')
            logger.write('\n')
        return return_value
    return wrapper

reverse = check_time(reverse)

def wrapper(*args, **kwargs):
    t1 = time.time()
    return_value = reverse(*args, **kwargs)
    t2 = time.time()
    with open('logfile.log', 'a') as logger:
        logger.write(f'{reverse.__name__} executed in {t2-t1}')
        logger.write('\n')
    return return_value

with open('logfile.log', 'a') as logger:
    logger.write('\n')
reverse([1,2,3,4])
wrapper([1,2,3,4])
"""