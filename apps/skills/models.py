from django.db import models


class Skill(models.Model):
    opciones = {
        ('dev', 'Desarrollo'),
        ('cgi', 'CGI')
    }

    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    porcentaje = models.PositiveIntegerField(default=50, verbose_name='Porcentaje')
    categoria = models.CharField(max_length=3, choices=opciones, verbose_name='Categoría')

    class Meta:
        db_table = "apps_skill"
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.nombre
