# Variables
my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# concatenacion de variables en un print
print(my_string_variable, str(my_int_variable),my_bool_variable)
print('Este es el valor de: ', my_bool_variable)

# Algunas funciones del sistema
print('my_string_variable len:',len(my_string_variable))

# variables en una sola linea. NO ABUSAR DE ESTA SINTAXIS
name,surname,alias,age='Alejandro','Rios','Rivers',23.0
print('Me llamo:',name,surname,'mi edad es:',age,'y mi alias es:',alias)

# inputs
name = input('Whats your name ?')
age = input('How old are you ?')
print(name,age)

# Cambiar tipo
name = 123
age = 'Rivers'
print(name,age)

# Forzado del tipo ?
address: str = 'Mi direccion' # solo es como un comentario :v # el tipado de python es dinamico
print(address)
address = 32
print(address)
print(type(address))