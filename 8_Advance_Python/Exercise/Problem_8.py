'''
Write a program to filter a list of numbers which are divisible by 5. 
'''

numbers = [1, 2, 3, 4, 5, 50, 100, 150, 200, 250]

divisible_by_5 = list(filter(lambda x: x%5 == 0, numbers))
print(divisible_by_5)