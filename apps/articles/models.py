from django.db import models
from core.utils import get_unique_slug

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción')
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        db_table = 'apps_categoria'
        verbose_name_plural = 'Categorías'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'nombre', 'slug')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('views.details', args=[self.slug])

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='publishing', null=True)
    categorias = models.ManyToManyField(Categoria)
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        db_table = 'apps_articulo'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'titulo', 'slug')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('views.details', args=[self.slug])

    def __str__(self):
        return self.titulo