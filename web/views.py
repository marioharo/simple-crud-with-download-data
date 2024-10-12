from django.shortcuts import render, redirect
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

def eliminar(request):
    ...