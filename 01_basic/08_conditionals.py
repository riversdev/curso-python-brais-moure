# conditionals
my_condition = True

if my_condition:
    print('Se ejecuta la condicion del if')

my_condition = 5 * 5

if my_condition == 10:
    print('Se ejecuta la condicion del segundo if')

if my_condition > 10:
    print('Se ejecuta la condicion del tercer if')
else:
    print('NO se ejecuta la condicion del tercer if')

if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20')
elif my_condition == 25:
    print('Es igual a 25')
else:
    print('Es menor o igual a 10 o mayor o igual a 20')

print('La ejecucion continua')


my_string = ''

if not my_string:
    print('El string es vacio')

if my_string:
    print('El string no es vacio')