# challenges
'''
FIZZBUZZ
Escribe un programa que muestre por consola (con un print) los
numeros de 1 a 100 (ambos incluidos) con un salto de linea entre
cada impresion, sustituyendo los siguientes:
    - multiplos de 3 por la palabra 'fizz'
    - multiplos de 5 por la palabra 'buzz'
    - multiplos de 3 y 5 a la vez por la palabra 'fizzbuzz'
'''
print('########### fizzbuzz')
# me
# def fizzbuzz():
#     for i in range(1, 101):
#         text = ''

#         if i % 3 == 0:
#             text += 'fizz'
        
#         if i % 5 == 0:
#             text += 'buzz'
        
#         if i % 3 != 0 and i % 5 != 0:
#             text = i
        
#         print(text)

# brais
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

# fizzbuzz()



'''
ES UN ANAGRAMA ?
Escribe una funcion que reciba dos palabras (String) y retorne
verdadero o falso (bool) segun sean o no anagramas.
    - Un anagrama consiste en formar una palabra reordenando TODAS
      las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
'''
print('########### isAnagram ?')
## me
# def is_anagram(word, anagram):
#     word = list(word.lower())
#     anagram = list(anagram.lower())

#     if word == anagram:
#         return False

#     for letter in anagram:
#         if not letter in word:
#             return False
#         word.remove(letter)
    
#     return len(word) == 0

# brais
def is_anagram(word, anagram):
    word = word.lower()
    anagram = anagram.lower()

    if word == anagram:
        return False
    
    return sorted(word) == sorted(anagram)

# me
# def is_anagram(word, anagram):
#     word, anagram = word.lower(), anagram.lower()

#     return sorted(word) == sorted(anagram) and not word == anagram

# print(is_anagram('perro', 'rerpo')) # True
# print(is_anagram('amor', 'Roma')) # True
# print(is_anagram('hello', 'hallo')) # False
# print(is_anagram('rivers', 'rivers')) # False
# print(is_anagram('riversdev', 'rivers')) # False



'''
FIBONACCI
Escribe un programa que imprima los 50 primeros numeros de la sucesion
de Fibonacci empezando en 0.
    - La serie de Fibonacci se compone por una sucesion de numeros en
      la que el siguiente numero siempre es la suma de los dos anteriores.
    - 0, 1, 1, 2, 3, 5, 8, 13...
'''
print('########### Fibonacci')
# me
# def Fibonacci(range_f, succession = [0, 1]):
#     if len(succession) == range_f:
#         return print(succession)

#     succession.append(succession[-1] + succession[-2])
#     Fibonacci(range_f, succession)
# Fibonacci(50)

# brais
def Fibonacci():
    prev = 0
    next = 1

    for i in range(0, 50):
        print(prev)

        latest = prev + next
        prev = next
        next = latest

# Fibonacci()



'''
NUMERO PRIMO
Escribe un programa que se encargue de comprobar si un numero es o no primo.
    - Hecho esto, imprime los numero primos entre 1 y 100
Un número primo es un número natural mayor que 1 
que tiene únicamente dos divisores positivos distintos: él mismo y el 1
'''
print('########### numero primo')
# brais
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num): # de esta manera se omite el mismo numero y el 1 (ya que el rango va desde el 2 hasta uno antes del numero)
        if num % i == 0: # si existe un numero por el que es entero divisible entonces NO ES primo, es compuesto
            return False
    
    return True

def print_primes(first, latest):
    for i in range(first, latest):
        if is_prime(i):
            print(i)

# print_primes(1, 100)



'''
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automatica.
    - Si le pasamos "Hola mundo" debe retornar "odnum aloh"
'''
print('########### invirtiendo cadenas')
# me
# def reverse_text(text):
#     text = list(text)
#     reverse_text = ''
#     c = len(text) - 1

#     while c >= 0:
#         reverse_text += text[c]
#         c -= 1
    
#     return reverse_text

# print(reverse_text('Hola mundo'))
# print(reverse_text('Rivers'))

# brais
def reverse(text):
    text_len = len(text)
    reversed_text = ''

    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]

    return reversed_text

# print(reverse('Hola mundo'))