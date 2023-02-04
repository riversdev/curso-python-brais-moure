# python package manager
# pip # https://pypi.org

# pip install --upgrade pip     # actualizar la version de pip
# pip list                      # paquetes instalados
# pip install pandas            # instalar pandas
# pip uninstall pandas          # desinstalar pandas
# pip show numpy                # ver detalles del paquete


# numpy
import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(numpy_array)
print(type(numpy_array))

print(numpy_array * 2)



# pandas
import pandas



# requests
import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(response)
print(response.status_code)
print(response.json())



# custom package # Arithmetics
from mypackage import arithmetics
from my_other_package import other_arithmetics

print(arithmetics.sum_two_values(1, 4))
print(other_arithmetics.sum_two_values(1, 4))