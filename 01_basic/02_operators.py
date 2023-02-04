# Operadores
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # modulo
print(10 // 3) # division a entero
print(2 ** 3) # potencia
print(2 ** 3 + 3 - 7 / 1 // 4)

print('Hola' + ' ' + 'Python')
print('Hola' + str(5))
print('Hola' * 5) # HolaHolaHolaHolaHola # es posible multiplicar los strings pero solo por numeros enteros

print('###############################')
print('### Operadores comparativos ###')
print('###############################')
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)

print('Hola' > 'Python')
print('Hola' < 'Python')
print('Hola' >= 'Python')
print('Hola' <= 'Python')
print('Hola' == 'Python')
print('Hola' != 'Python')

print('zaaa' >= 'baaa') # se basa en ordenacion alfabetica por ASCII
print(len('aaaa') >= len('babb')) # contar caracteres

print('###############################')
print('### Operadores logicos ###')
print('###############################')
print(6 > 4 and 'Hola' > 'Python') # &&
print(6 > 4 or 'Hola' > 'Python') # ||
print(3 < 4 and 'Hola' > 'Python' and 4 == 4)
print(3 > 4)
print(not (3 > 4)) # negacion