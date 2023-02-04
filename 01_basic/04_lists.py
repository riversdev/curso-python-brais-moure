# lists
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(len(my_list))
print(my_list)

my_other_list = [35, 1.77, 'Alejandro', 'Rios']
print(type(my_list)) # list
print(type(my_other_list)) # list

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
# print(my_other_list[-5]) # IndexError
# print(my_other_list[4]) # IndexError

print(len(my_other_list)) # retorna la longitud
print(my_other_list.count('Rios')) # retorna el conteo de los que son iguales al parametro

print(my_other_list[len(my_other_list) - 1])

age, height, name, surname = my_other_list # desestructuracion pero se deben crear variables de TODAS las posiciones de la lista
print(age, height, name, surname)

height, name, height, surname = my_other_list[0], my_other_list[2], my_other_list[1], my_other_list[3] # preferible no usar esa forma 
print(age, height, name, surname)

new_list = my_list + my_other_list # concatenacion de listas
print(type(new_list), new_list)

# agregar elementos
my_other_list.append('MoureDev') # al final
print(my_other_list)

my_other_list.insert(1, 'Azul') # en una posicion
print(my_other_list)


# eliminar elementos
my_other_list.remove('Azul') # eliminar un elemento por valor y solo el primer elemento que encuentre
print(my_other_list)

popValue = my_other_list.pop() # al final y pop() retorna lo que elimino
print(my_other_list, popValue)

popValue = my_other_list.pop(2) # el parametro a pop es el indice a eliminar
print(my_other_list, popValue)

del my_other_list[2] # eliminar un elemento por indice pero sin retornar nada
print(my_other_list)

my_other_list.clear() # limpiar la lista
print(my_other_list)

my_other_list = [35, 1.77, 'Alejandro', 'Rios']
my_other_list.insert(1, 'Azul')

my_new_list = my_other_list.copy() # se crea una nueva lista (ya no mantiene la referencia)
print(my_new_list)

my_new_list.reverse() # darle vuelta a la lista
print(my_new_list)

sort_var = [4,2,56,8.6]
sort_var.sort() # ordenar pero solo numeros o solo strings
print(sort_var)

print(my_new_list[2:4]) # extraer los elementos entre los indices 2 y 4