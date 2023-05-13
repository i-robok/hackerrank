#!/bin/python3

import sys
from datetime import datetime

def multiples_3_5(n):
    suma = 0

    n_3 = int((n - 1) / 3)
    n_5 = int((n - 1) / 5)
    n_15 = int((n - 1) / 15)

    suma = (3 * (n_3 * (n_3 + 1)//2))
    print(f'{suma}')
    suma += (5 * (n_5 * (n_5 + 1)//2))
    print(f'{suma}')
    suma -= (15 * (n_15 * (n_15 + 1)//2))
    print(f'{suma}')
            
    return suma

def multiples(n: int) -> int:

    suma = 0
 
    suma += sum(range(3,n,3))
    print(f'{suma}')

    suma += sum(range(5,n,5))
    print(f'{suma}')

    suma -= sum(range(15,n,15))
    print(f'{suma}')

    return(suma)

def lento(n: int) -> int:
    suma = 0
    for x in range(1,n):
        if (x % 3 == 0) or (x % 5 == 0):
            suma += x

    return (suma)

n = 1000
# n = 100

print(f'{datetime.now()}')
print(f'{multiples_3_5(n)}')
print(f'{datetime.now()}')
print(f'{multiples(n)}')
print(f'{datetime.now()}')
# print(f'{lento(n)}')
print(f'{datetime.now()}')

'''
n = 999999999
n -= 1
print(f'{datetime.now()}')
print(f'{multiples_3_5(n)}')
print(f'{datetime.now()}')
print(f'{multiples(n)}')
print(f'{datetime.now()}')
# print(f'{lento(n)}')
print(f'{datetime.now()}')
'''