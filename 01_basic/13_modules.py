# modules

# importar todo el modulo
import my_module

my_module.sumValues(5, 3, 6)
my_module.printValue('Hello')



# importar desestructurado
from my_module import sumValues, printValue

sumValues(5, 3, 6)
printValue('Hello Python')



# modulos del sistema
import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE

print(PI_VALUE)