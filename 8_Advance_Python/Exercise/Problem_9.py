'''
Write a program to find the maximum of the numbers in a list using the reduce 
function. 
'''

from functools import reduce
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

max_num = reduce(lambda a, b: a if a > b else b, list)
print(max_num)