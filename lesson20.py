def factorial(n):
    """
    !5 = 5 * 4 * 3 * 2 * 1
    1 call factorial(5)
    => 5 * factorial(4) P1
    2 call factorial(4)
    => 4 * factorial(3)
    3 call factorial(3)
    => 3 * factorial(2)
    4 call factorial(2)
    => 2 * factorial(1)
    5 call factorial(1)
    => 1! == 1 =>
    """
    if n == 1:
        return n
    return n * factorial(n-1)

def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        x, y = y, x + y
    print(x)
    """
    n = 5
    [1, 1, 2, 3, 5]

    """

def fibonacci_rec(n, x=0, y=1):
    """
    1 call fibonacci_rec
    => 1
    n = 5

    x = 0
    y = 1
    2 call
    => 1 
    n = 4
    x = 1
    y = 1
    3 call
    n = 3
    x = 1
    y = 2
    4 call
    n = 2
    x = 2
    y = 3
    5 call

    """
    if n == 0:
        return
    print(y)
    fibonacci_rec(n-1, y, x + y)
    
def fibonacci_user(n):
    """
    1 call
    n = 5
    2 cal
    """
    if n <= 2:
        return 1
    return fibonacci_user(n-1) + fibonacci_user(n-2)


def print_reverse(n: list):
    """
    n > [1,2,3,4,5]
    function will print
    5
    4
    3
    2
    1
    """
    if len(n) == 0:
        return
    print(n[-1])
    print_reverse(n[0:-1])
    print('_')
    print(n)

def polindrom(s: str) -> bool:
    """
    aba
    a|n|d|n|a
    a|s|a|dd|a|s|a
    ....
    """
    if len(s) == 0:
        return False
    if len(s) == 1:
        return True

    if s[0] == s[-1]:
        if len(s) == 2:
            return True
        return polindrom(s[1:-1])
    return False


def polindrom2(my_str: str) -> bool:
    if len(my_str) == 0:
        return False
    if len(my_str) == 1:
        return True
    if my_str[0] != my_str[-1]:
        return False
    elif len(my_str)== 2:
        return True
    return polindrom2(my_str[1:-1])

print_reverse([1,2,3,4,5])


def function3():
    return 2

def function1():
    function3()
    return 1

def function2():
    print(0)
    print(function1())
    print(2)

function2()
print(f'6! = {factorial(6)}')


fibonacci_rec(6)
print('______')
print(fibonacci_user(6))


print(polindrom("adasada"))
print(polindrom2("adassada"))