from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="projects", verbose_name="Imagen")
    link = models.URLField(null=True, blank=True, verbose_name="Enlace (GitHub/Demo)")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
    


class Message(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Nombre Completo")
    email = models.EmailField(verbose_name="Correo Electrónico")
    subject = models.CharField(max_length=150, verbose_name="Asunto")
    content = models.TextField(verbose_name="Mensaje")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Enviado el")
    is_read = models.BooleanField(default=False, verbose_name="Leído")

    class Meta:
        verbose_name = "mensaje"
        verbose_name_plural = "mensajes"
        ordering = ["-sent_at"]

    def __str__(self):
        return f"{self.full_name} - {self.subject}"