# exceptions
# Exception Handling
numberOne = 5
numberTwo = 1
numberTwo = '1'

try:
    print(numberOne + numberTwo)
except:
    print('Exception')


try:
    print(numberOne + numberTwo)
except:
    print('Exception')
else: # else en try se ejecuta solo si no se produce una exepcion
    print('La ejecucion continua')


try:
    print(numberOne + numberTwo)
except:
    print('Exception')
else: # else en try se ejecuta solo si no se produce una exepcion
    print('La ejecucion continua')
finally: # se ejecuta siempre
    print('Finally del try')


# else y finally son opcionales pero el try y except no
# SI HAY UN TRY DEBE HABER UN EXCEPT


# Exceptions por tipo
try:
    print(numberOne + numberTwo)
except TypeError: # capturar solo errores de tipo TypeError
    print('Se ha producido un error')


'''
Tipos
    ValueError
    TypeError
'''

# captura de la exepcion
try:
    print(numberOne + numberTwo)
# except TypeError as e:
    # print('Se ha producido un error: ', e)
# except ValueError as e:
    # print('Se ha producido un error: ', e)
except Exception as e: # cualquier exepcion ######################
    print('Se ha producido un error: ', e)