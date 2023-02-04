# dicts
my_dict = dict()
my_other_dict = {}

print(type(my_dict), type(my_other_dict))

my_other_dict = {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}
my_dict = {
    'Nombre': 'Brais', 
    'Apellido': 'Moure', 
    'Edad': 35, 
    'Lenguajes': {'Python', 'Swift', 'Kotlin'},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_dict))

print(my_dict['Nombre'])

my_dict['Nombre'] = 'Rivers'
print(my_dict['Nombre'])

print(my_dict[1])

my_dict['Calle'] = 'Calle MoureDev'
print(my_dict)

del my_dict['Calle'] # eliminar un par clave valor del objeto # del dict xd
print(my_dict)

print('Moure' in my_dict)
print('Mouri' in my_dict)
print('Apellido' in my_dict)
print('Python' in my_dict['Lenguajes'])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(('Nombre', 1, 'Piso')) # crear un diccionario con estas claves
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) # asi se crea una copia de un dict pero sin sus valores
print(my_new_dict)

# dict.fromkeys acepta listas, tuplas, diccionarios. para crear un nuevo diccionario con esas claves pero sin valores

my_new_dict = dict.fromkeys(my_dict, ['Brais', 'Moure']) # el segundo algumento de dict.fromkeys se asigna como valor a todas las claves del dict
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values)) # dict_values
print(list(my_values)) # dict_values a lista ej # aqui aparece una lista de listas [Brais, Moure] porque asi se definio en la linea 51 fromkeys al crear my_new_dict

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))

print(list(dict.fromkeys(list(my_other_dict.values())).keys()))