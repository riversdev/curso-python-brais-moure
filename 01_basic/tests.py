# valores de True y False en numero
print(True == 1) # True
print(False == 0) # True
print(('Uno', 'Dos')[False]) # Uno
print(('Uno', 'Dos')[True]) # Dos


# ordenar
print('#################### ordenamiento')
print(sorted([3,6,1,-5,40])) # [-5, 1, 3, 6, 40]
print(sorted('hello')) # ['e', 'h', 'l', 'l', 'o']


# variable _
_ = 'Hi'
print(_)


print('#################### fibonacci por numero de iteraciones')
def fibonacci(rangef, curr = 0, succession = [0, 1]):
    if len(succession) == rangef:
        return print(succession)
    
    succession.append(succession[-1] + succession [-2])
    fibonacci(rangef, curr + 1, succession)

fibonacci(15)


print('#################### fibonacci por rango')
from math import sqrt

def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def Fibonacci(startNumber, endNumber):
    n = 0
    cur = F(n)

    while cur <= endNumber:
        if startNumber <= cur:
            print(cur)
            
        n += 1
        cur = F(n)

Fibonacci(10, 500)



print('################### ReGex')
import re

cad = 'Esta es una 3 cadena Accounting5'

print(re.search('Accounting|[0-9]', cad))