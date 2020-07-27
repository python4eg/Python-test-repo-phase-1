import time

def function1():
    a = 2
    while True:
        a *= a
        time.sleep(3)
        yield a


def function2():
    a = 1
    while True:
        a += 1
        time.sleep(3)
        yield a


queue = list()
queue.append(function1())
queue.append(function2())

while True:
    print(f'f1: {next(queue[0])}')
    print(f'f2: {next(queue[1])}')
    print()