# loops

# while
counter = 0

while counter < 10:
    print(counter)
    counter += 1
else:
    print('Mi contador es mayor o igual a 10') # al terminar YES

print('La ejecucion continua')


while counter < 20:
    counter += 1

    if counter == 15:
        print('El contador es 15')
        break

    print(counter)

print('La ejecucion continua')


# for
my_list = [35, 24, 62, 52, 30, 30, 17]
my_tuple = ('H', 'e', 'l', 'l', 'o')
my_set = {'Brais', 'Moure', 35}
my_dict = {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}

for element in my_list:
    print(element)

for element in my_tuple:
    print(element)

for element in my_set:
    print(element)

print('########## dict keys')
for element in my_dict: # claves del dict
    print(element)

print('########## dict values')
for element in my_dict.values(): # valores del dict
    print(element)
    if element == 'Moure':
        continue # continua con la siguiente iteracion
    if element == 35:
        break # detiene todo el bucle
    print('Ultima linea del for')
else:
    print('El for se ha terminado')


print('La ejecucion continua')