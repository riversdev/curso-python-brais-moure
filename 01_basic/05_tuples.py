# tuples
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, 'Brais', 'Moure', 'Brais')
my_other_tuple = (30, 60, 15)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) # IndexError
# print(my_tuple[-6]) # IndexError

print(my_tuple.count('Brais'))
print(my_tuple.index('Moure'))
print(my_tuple.index('Brais')) # el primer indice que coincide

# my_tuple[1] = 1.80 # es INMUTABLE #######################################################
print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

# solo asi es posible mutar una tupla
# cambiando el tipo a una lista, hacer los cambios 
# y luego devolver a tipo tuple
my_list = list(my_tuple)
my_list[4] = 'MoureDev'
my_list.insert(1, 'Azul')
print(my_list)
my_tuple = tuple(my_list)
print(type(my_tuple))

del my_tuple
# print(my_tuple) # asi se elimina una variable