import sys

from module1 import sqr_numbers

print(sqr_numbers(3, 2))

print(sys.path)

my_direct = '/Users/dmitrii/Documents/Beetroot/python-learning/Homework/lesson3/'
sys.path.append(my_direct)
print(sys.path)


import module1
print(module1.sqr_numbers(2, 8))