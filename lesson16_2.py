import os
import sys

curr_dir = os.getcwd()
print(f'Current dir: {curr_dir}')

prev_dir = os.path.join(curr_dir, '..')
print(f'Previous dir relative path {prev_dir}')

prev_abs_dir = os.path.abspath(prev_dir)
print(f'Previous dir absolute path {prev_abs_dir}')

prev_rel_dir = os.path.relpath(prev_abs_dir)
print(f'Previous dir relative path from current directory {prev_rel_dir}')

file_name = 'new.json'
print(f'Does file {file_name} exist: {os.path.exists(file_name)}')

file_name_abs_path = os.path.abspath(file_name)
print(file_name_abs_path)

print(sys.path)
sys.path.insert(0, prev_abs_dir)
print(sys.path)

def in_range(start, end, step=1):
    if start > end and step >= 1:
        return []
for i in range(20, 10, 6):
    print(i)

def enum(iterations, start=0):
    index = start
    iterations.append(1000)
    for i in iterations:
        yield index, i
        index += 1

g = [1,2,3,4,5,6]
print(list(enum(g, 3)))
print(g)

# Most known
import argparse
import collections
import contextlib
import itertools
import functools
import optparse
import os
import sys

#Danger zone
import re


class Building(object):
     def __init__(self, floors):
         self._floors = ['' for i in range(floors)] # OR ['']*floors
     def __setitem__(self, floor_number, data):
          self._floors[floor_number] = data
     def __getitem__(self, floor_number):
          return self._floors[floor_number]
building1 = Building(4) # Construct a building with 4 floors
building1[0] = 'Reception'
building1[1] = 'ABC Corp'
building1[2] = 'DEF Inc'
print( building1[2] )