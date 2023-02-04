# classes
class MyEmptyPerson:
    pass # para permitir un bloque de codigo que no tiene nada

print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, alias = 'Sin alias'): # constructor de clase # self hace referencia a la misma clase # como el this
        self.__name = name # prop privada # pero si se puede modificar desde dentro de la clase
        self.__surname = surname
        self.full_name = f'{name} {surname} ({alias})' # prop publica

    def walk(self):
        print(f'{self.full_name} esta caminando')
    
    def get_name(self): # set para obtener el name que es una prop privada
        # self.__name = 'HIHII'
        return self.__name


my_person = Person('Alejandro', 'Rios')
print(my_person.full_name)
my_person.walk()
print(my_person.get_name())

my_other_person = Person('Brais', 'Moure', 'MoureDev')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Hector de Leon (el loco de los perros)'
print(my_other_person.full_name)
my_other_person.full_name = 666
print(my_other_person.full_name)