def function_name(args_1, args_2, x, y):
    print(x, y)
    print(args_1, args_2)
    return args_1, args_2
    return 'Ababagalamaga'

def function_name2(args_1, args_2):
    x = 200
    y = 200
    print(args_1, args_2)
    return args_1, args_2
    return 'Ababagalamaga'

x = 2000
y = 2000
while True:
    function_name(20, 10, x, y)
    break
print(function_name(1, 3, x, y))

def pack(a, *args, b, **kwargs):
    print(a)
    print(args)
    print(b)
    print(kwargs)

pack(1, 2, 3, 4, 5, 6, b=2, v=2)



def pack(a, b, *, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

pack(1, 2, c=3, d=4)


def number_or_zero(a):
    if a.isdigit():
        return int(a)
    return 0

def sum(a, b):
    return number_or_zero(a) + number_or_zero(b)


sum_l = lambda a, b: number_or_zero(a) + number_or_zero(b)
print(sum('1', '2'))

li = [{'a': 10},  {'a': 2},]
li.sort(key=lambda a: a['a'])
print(li)

