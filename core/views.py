from django.shortcuts import render
from django.views.generic import TemplateView
from apps.skills.models import Skill
from apps.social_media.models import SocialMedia
from apps.slider.models import Slider
from apps.articles.models import Articulo


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habilidades_dev'] = Skill.objects.filter(categoria='dev')
        context['habilidades_cgi'] = Skill.objects.filter(categoria='cgi')
        context['medios_sociales'] = SocialMedia.objects.all()
        context['slider'] = Slider.objects.all()
        context['proyectos'] = Articulo.objects.filter(categorias=3)
        return context
