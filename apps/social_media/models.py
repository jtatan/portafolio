from django.db import models


class SocialMedia(models.Model):
    redes = {
        ('FB', 'Facebook'),
        ('PI', 'Pinterest'),
        ('WA', 'Whatsapp'),
        ('IG', 'Instagram'),
        ('LI', 'Linkedin'),
        ('BH', 'Behance'),
        ('DA', 'Devian Art')
    }

    nombre = models.CharField(max_length=2, choices=redes, verbose_name='Nombre')
    enlace = models.URLField(verbose_name='URL de la Red Social')
    imagen = models.ImageField(upload_to='medios_sociales', default='', null=True, blank=True, verbose_name='Imágen')

    class Meta:
        db_table = "apps_socialmedia"
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.nombre
