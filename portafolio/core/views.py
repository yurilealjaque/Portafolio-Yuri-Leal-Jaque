from django.shortcuts import render, redirect  # Agregamos redirect
from .models import Project
from .forms import ContactForm  # Importante: Importamos el formulario que creamos

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def portafolio(request):
    # Traemos los proyectos de Postgres
    projects = Project.objects.all()
    return render(request, 'core/portafolio.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el mensaje en la base de datos PostgreSQL
            # Por ahora, redirigimos a 'home' o a una página de éxito si la tienes
            return redirect('home') 
    else:
        form = ContactForm()
    
    # Cambié 'tu_app/contacto.html' por la ruta que usas en tu proyecto
    return render(request, 'core/contact.html', {'form': form})