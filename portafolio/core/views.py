from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

# Esta es la única que debe quedar para el portafolio
def portafolio(request):
    # Traemos los proyectos de Postgres
    projects = Project.objects.all()
    # Los enviamos al HTML
    return render(request, 'core/portafolio.html', {'projects': projects})

def contact(request):
    return render(request, 'core/contact.html')