import glob
import os
from typing import Dict, List, Tuple, Union, Optional, Any, Iterable, Iterator

#os.chdir('d:\\')
##print(glob.glob('*git*'))
#print(os.listdir())
#print(glob.glob('**\\*z*', recursive=True))
#  **\\*z* for Windows and **/*z* for Unix and Mac
search_path = os.path.join('**', '*z*')

#print(glob.glob())
item = 2


# comment
def func(item=None):
    """Func doc """
    return item


func(item=1)


class Sample:
    def __init__(self):
        pass

    def smth(self):
        print('Hello')


def add(item1: float, item2: float) -> Union[float, int]:
    result = item1 + item2
    if type(result) == float and result.is_integer():
        return int(result)
    return result    

x = 1
y = 2

x = '1'
y = '2'

print(add(x, y))


def div(item1: Union[int, float], item2: int) -> float:
    """Comment"""
    return item1 / item2

x1 = input('X: ')
y1 = int(input('Y: '))
x_int = int(x1)
print(div(x_int, y1))

x2: float = 10.2
y2 = 12
print(div(x2, y2))


new_x: int = div(1,2)


def equal(item1: Any, item2: Any = None) -> bool:
    """Comment"""
    return item1 == item2

print(equal(1, '1'))


any_list: List[Union[int, str]] = [1, 2, 3, 4]
any_list.append('7')

help(equal)


def format(data: str, separator: Optional[str] = None) -> Union[Optional[str], List[str]]:
    if separator is not None:
        return data.strip().split(separator)
    if data.isalpha():
        return data.strip()
    return None

print(format('12344'))

StrToStrDict = Dict[Any, Dict]
Phonebook: StrToStrDict = {[1]: {'name': 'Sasha'}}
CellphoneBook: StrToStrDict = {'+343220': {'name': 'Sasha'}}

Pair = Tuple[int, int]
g: Pair = (1,2,3)

PairLisr = List[Pair]

# pip install mypy
# pip install flake8
# flake8 file.py - for style check
# mypy file.py - type hint 

