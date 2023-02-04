# error types

# SyntaxError
# print'Hello'
print('Hello')

# NameError
# print(name)
name = 'Rivers'
print(name)

# IndexError
my_list = ['Python', 'Swift', 'Kotlin', 'Dart', 'Javascript']
# print(my_list[10])
print(my_list[4])

# ModuleNotFoundError
# import maths
import math

# AttributeError
# print(math.PI)
print(math.pi)

# KeyError
my_dict = {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}
# print(my_dict['Apelido'])
print(my_dict['Edad'])

# TypeError
# print(my_list['4'])
print(my_list[4])

# ImportError
# from math import PI
from math import pi

# ValueError
# my_int = int('10RIVERS')
my_int = int('10')

# ZeroDivisionError
# print(4 / 0)
print(4 / 2)