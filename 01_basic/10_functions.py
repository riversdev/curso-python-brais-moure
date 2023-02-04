# functions
def my_function():
    print('Hello into function')

    def other_function():
        print('Hello into other function')

    return other_function

my_function()()


def sum_two_values(a: int, b: int): # el tipado es fantasia xd, y ayuda al linter
    return a + b

print(sum_two_values(1, 2))
print(sum_two_values('9', '5'))
print(sum_two_values(1.89, 3.56))

def print_name(name, surname):
    print(f'{name} {surname}')

print_name('Alejandro', 'Rios')
print_name(surname='Rios', name='Alejandro') # especificar los parametros

def print_name_with_default(name, surname, alias = 'Sin alias'): # admite valores por defecto en los parametros
    print(f'{name} {surname}, {alias}')

print_name_with_default('Alejandro', 'Rios', 'Rivers')
print_name_with_default('Alejandro', 'Rios')

def print_texts(*texts): # agrupar los parametros en una tupla
    # print(type(texts)) # tuple
    print(texts)

    for text in texts:
        print(text.upper())

print_texts('Hello')
print_texts('Hello','Python','Moure')