from django.shortcuts import render
from django.views.generic import TemplateView
from apps.skills.models import Skill
from apps.social_media.models import SocialMedia


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habilidades_dev'] = Skill.objects.filter(categoria='dev')
        context['habilidades_cgi'] = Skill.objects.filter(categoria='cgi')
        context['medios_sociales'] = SocialMedia.objects.all()
        return context
