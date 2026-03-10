from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portafolio/', views.portafolio, name='portafolio'),
    # Agregamos la barra diagonal al final de 'contact/' por consistencia en Django
    path('contact/', views.contact, name='contact'),
    path('proyecto/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)