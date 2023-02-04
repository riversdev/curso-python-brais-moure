# regular expressions
import re

my_string = 'Esta es la leccion numero 7: Leccion llamada: Expresiones regulares.'
my_other_string = 'Esta no es la leccion numero 6: Manejo de ficheros.'

print('####################### match')
# match solo busca al inicio de la cadena # crea una tupla
print(re.match('Esta es la leccion', my_string)) # Match
print(re.match('Esta es la leccion', my_other_string)) # None
print(re.match('Expresiones regulares', my_string)) # None

match = re.match('Esta es la leccion', my_string)
print(match)

span = match.span() # rango
print(type(span), span)

start, end = span
print(start, end)

print(my_string[start:end]) # extraccion del rango en la cadena



# search
print('####################### search')
# search lo busca donde sea en el string # crea una tupla
search = re.search('leccion', my_string, re.I) # re.I ignora entre minusculas y mayusculas
print(search)

start, end = search.span()
print(my_string[start:end])



# findall
print('####################### findall')
# findall encuentra todas las coincidencias en el string # crea una lista
findall = re.findall('leccion', my_string, re.I)
print(findall)



# split
print('####################### split')
# split separa el string por el caracter en el parametro # crea una lista
split = re.split(' ', my_string)
print(split)



# sub
print('####################### sub')
# sub sustituye las coincidencias en la cadena, retorna el nuevo string y deja intacto el original
sub = re.sub('Expresiones regulares', 'RegEx', my_string)
print(sub, my_string)

subAll = re.sub('leccion|Leccion', 'LECCION', my_string) # manera de cambiar varias palabras por una
print(subAll)

subAll = re.sub('[l|L]eccion', 'LECCION', my_string) # manera de cambiar varias palabras por una con una modificacion
print(subAll)



# patterns
print('####################### patterns')
# https://regex101.com # para validar regex
pattern = r'[lL]eccion'
print(re.findall(pattern, my_string))

pattern = r'[lL]eccion|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))

pattern = r'[a-zA-Z]'
print(re.match(pattern, my_string))

pattern = r'[0-9]'
print(re.search(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].'
print(re.findall(pattern, my_string))

pattern = r'[l]..'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.search(pattern, my_string))



# email validation regular expression (regex)
print('####################### email validation regex')

pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

email = 'hello@mail.com'
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = 'hello@mail'
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))