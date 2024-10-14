import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utilities import cleaned_data
from .models import Persona

# Create your views here.
def home(request):
    if request.method == 'GET':
        personas = Persona.objects.all()
        context = {'personas' : personas}
        return render(request, 'home.html', context)
    else:
        data = cleaned_data(request.POST)
        Persona.objects.create(**data)
        return redirect('/')
    
def editar(request, id):
    if request.method == 'GET':
        persona = Persona.objects.get(id = id)
        context = {'persona': persona}
        return render(request, 'editar.html', context)
    else:
        pk = request.POST['id']
        data = cleaned_data(request.POST)
        persona = Persona.objects.filter(id = pk)
        persona.update(**data)
        return redirect('/')

def eliminar(request, id):
    Persona.objects.get(id = id).delete()
    return redirect('/')


def descargar(request):
    personas = Persona.objects.all() # traemos toda la data
    """Aquí empieza la creación del documento"""
    # Crear la respuesta HTTP con el tipo de contenido correcto
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="descarga.csv"'
    # Crear el escritor CSV
    data = csv.writer(response)
    HEADER = [field.name for field in Persona._meta.fields if field.name != 'id'] # encabezados (quitando la columna 'id')
    # Escribimos los datos
    data.writerow(HEADER)
    for persona in personas:
        row = [getattr(persona, field) for field in HEADER] # todas las filas con la información
        data.writerow(row)
        
    return response