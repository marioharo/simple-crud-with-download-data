from django.shortcuts import render, redirect
from .models import Persona

# Create your views here.
def home(request):
    if request.method == 'GET':
        personas = Persona.objects.all()
        context = {'personas' : personas}
        return render(request, 'home.html', context)
    else:
        Persona.objects.create(
            nombre_completo = request.POST['nombre_completo'],
            peso = request.POST['peso'],
            talla = request.POST['talla'],
        )
        return redirect('/')