import csv
from .models import Persona

### Cargar datos para poblar db ###
def import_data():
    with open('personas_crud.csv', 'r') as file:
        data = csv.reader(file, delimiter=';')
        data = list(data)
    data.pop(0) #quita los encabezados
    for d in data:
        Persona.objects.create(
            #variables de acuerdo al db model
            nombre_completo = d[0],
            peso = d[1],
            talla = d[2],
            )


### Recoge toda la data del formulario como dict sin el token ###
cleaned_data = lambda x:{k:v for k,v in x.items() if k != 'csrfmiddlewaretoken'}