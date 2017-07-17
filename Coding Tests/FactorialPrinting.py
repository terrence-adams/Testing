__author__ = 'adam0954'
'''
Demonstrates nested loops and factorials
'''

def factorial_printing(x):
    if x > 0:
        for i in range(1, x + 1):
            for j in range(i):
                print('*', end='') #  end ='' is required for Python 3
            print('\n')
    else:
        return x


factorial_printing(12)