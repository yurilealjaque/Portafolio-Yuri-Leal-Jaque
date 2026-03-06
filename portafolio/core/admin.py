
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Esto muestra estos campos en la lista principal del admin
    list_display = ('title', 'created', 'updated')
    # Estos campos se verán en el formulario pero no se podrán editar
    readonly_fields = ('created', 'updated')
    # Añade una barra de búsqueda por título
    search_fields = ('title',)