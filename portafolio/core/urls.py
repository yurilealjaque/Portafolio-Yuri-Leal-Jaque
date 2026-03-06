from django.urls import path
from . import views
from django.conf import settings # <--- ESTA ES LA QUE TE FALTA
from django.conf.urls.static import static # <--- Y ESTA PARA LAS IMÁGENES

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name= 'about'),
    path('portafolio/', views.portafolio, name='portafolio'),
    path('contact', views.contact, name= 'contact' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)