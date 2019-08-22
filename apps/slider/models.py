from django.db import models

class Slider(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    cuerpo = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(upload_to='slider', verbose_name='Imagen Slider')

    class Meta:
        db_table = "Slider"
        verbose_name = 'Slider'
        verbose_name_plural = 'Publicaciones de Slider'

    def __str__(self):
        return str(self.imagen)

