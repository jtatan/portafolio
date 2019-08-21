from django.db import models

class Skill(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    porcentaje = models.PositiveIntegerField(default=50, verbose_name='Porcentaje')

    class Meta:
        db_table = "Skill"
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.nombre