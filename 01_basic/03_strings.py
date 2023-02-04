### Strings ###
my_string = 'Mi String'
my_other_string = 'Mi String'

print(len(my_string))
print(len(my_other_string))

print (my_string + ' ' + my_other_string)

my_new_line_string = 'Este es un string \n con salto de linea'
print(my_new_line_string)

my_tab_string = 'Este es un string \t con tabulacion'
print(my_tab_string)

my_scape_string = '\\tEste es un string \\n con escapado'
print(my_scape_string)

print('###############################')
print('########### formateo ##########')
print('###############################')
name, surname, age = 'Alejandro', 'Rios', 23
print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age)) # de preferencia usar esto
print('Mi nombre es ' + name + ' ' + surname + ' y mi edad es ' + str(age)) # de preferencia asi no !!!
print(f'Mi nombre es {name} {surname} y mi edad es {age + 5}') # USAR ESTA FORMA XDXD ####################################

print('###############################')
print(' desempaquetado de caracteres #')
print('###############################')
language = 'Python'
a, b, c, d, e, f = language

print(a)
print(b)
print(c)

print('###############################')
print('########### division ##########')
print('###############################')
language_slice = language[1:3] # slice desde el 1 hasta el 3
print(language_slice)

language_slice = language[1:] # slice desde 1 hasta el final
print(language_slice)

language_slice = language[-2] # slice tomando la posicion -2
print(language_slice)

language_slice = language[0:6:2] # slice desde 0 hasta 6 (todo) seleccionando de 2 en 2
print(language_slice)

print('###############################')
print('########### reverse ###########')
print('###############################')
language_reverse = language[::-1] # hacer reversa
print(language_reverse)

print('###############################')
print('########## funciones ##########')
print('###############################')
cadena = 'hEllo'
print(cadena.capitalize())
print(cadena.upper())
print(cadena.lower())
print(cadena.count('l')) # cuantas 'l' tiene
print(cadena.isnumeric()) # si podria ser numero
print(cadena.isupper())
print(cadena.upper().isupper())
print(cadena.startswith('hE'))
print('Python' == 'python') # false