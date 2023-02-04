# file handling

import os

# .txt file
txt_file = open('./06_my_file.txt', 'w+') # leer y escribir
txt_file.write('Mi nombre es Alejandro\nMi apellido es Rios\nMi edad es 23 anios\nY mi lenguaje preferido es JavaScript alv')

txt_file.close() # cerrar el fichero # despues de escribir se puede cerrar para que la proxima lectura comience en la primera linea, porque siempre mantiene el cursor en el ultimo lugar donde se escribio o leyo
txt_file = open('./06_my_file.txt', 'r+') # leer

# print(txt_file.read(10)) # leer los primeros 10 caracteres
# print(txt_file.read()) # leer el resto del archivo

print(txt_file.readline()) # leer una linea
# print(txt_file.readline())
# print(txt_file.readlines()) # leer todas las lineas

for line in txt_file.readlines(): # lee todas las lineas que quedan
    print(line)


txt_file.write('\nAunque tambien me gusta Python') # escribir una linea en el fichero # no es valido porque se abrio en modo solo lectura
print(txt_file.readline())

txt_file.close() # cerrar el fichero

# os.remove('./06_my_file.txt') # eliminar el fichero



# .json file
print('########################################################### json file')
import json

json_file = open('./06_my_file.json', 'w+')

json_test = {
    'name': 'Brais',
    'surname': 'Moure',
    'age': 35,
    'languages': ['Python', 'Swift', 'Kotlin'],
    'website': 'https://moure.dev'
}

json.dump(json_test, json_file, indent = 4)

json_file.close()
json_file = open('./06_my_file.json', 'r+')

for line in json_file.readlines():
    print(line)

json_dict = json.load(open('./06_my_file.json'))
print(json_dict)
print(type(json_dict))
print(json_dict['name'])



# .csv file
print('########################################################### csv file')
import csv

csv_file = open('./06_my_file.csv', 'w+')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'surname', 'age', 'languages', 'website'])
csv_writer.writerow(['Brais', 'Moure', 35, 'Python', 'https://moure.dev'])
csv_writer.writerow(['Roswell', '', 2, 'Cobol', ''])

csv_file.close()

csv_file = open('./06_my_file.csv', 'r+')

for line in csv_file.readlines():
    print(line)



# .xlsx file
print('########################################################### xlsx file')
# import xlrd # debe instalarse



# .xml file
print('########################################################### xml file')
import xml