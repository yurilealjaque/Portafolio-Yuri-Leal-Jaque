from django.contrib import admin
from .models import Project, Message  # Importamos los modelos desde models.py

# Configuración para el modelo Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    search_fields = ('title',)

# Configuración para el modelo Message
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # Usamos los nombres exactos que definiste en tu models.py
    list_display = ('full_name', 'email', 'subject', 'sent_at', 'is_read')
    readonly_fields = ('full_name', 'email', 'subject', 'content', 'sent_at')
    search_fields = ('full_name', 'email', 'subject')
    list_filter = ('is_read', 'sent_at')