# sets
my_set = set()
my_other_set = {} # inicialmente es un dict (diccionario)

print(type(my_set))
print(type(my_other_set))

my_other_set = {'Brais', 'Moure', 35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('MoureDev') # un set no es una estructura ordenada por lo que no se pueden consultar los valores por posicion
my_other_set.add('MoureDev') # un set no agrega repetidos
print(my_other_set)

print('Moure' in my_other_set) # verificar si un set contiene un valor
print('Mouri' in my_other_set)

my_other_set.remove('Moure')
print(my_other_set)

my_other_set.clear() # borra todos los elementos que tiene el set
print(my_other_set)


del my_other_set
# print(my_other_set)


my_set = {'Brais', 'Moure', 35} # no es ordenadooo
my_list = list(my_set) # si se convierte a lista esta tendra ya un orden pero al crearla el orden no es predecible
print(my_set, my_list[0])

my_other_set = {'Kotlin', 'Swift', 'Python'}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({'Javascript', 'C#'})) # no aparecen repetidos YES

print(my_new_set.difference(my_set)) # encontrar los diferentes