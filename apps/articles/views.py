from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Articulo


class ArticuloVista(ListView):
    model = Articulo
    template_name = 'labs.html'
    context_object_name = 'articulos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticuloDetalleVista(DetailView):
    template_name = 'labs/articulos.html'
    queryset = Articulo.objects.all()
    context_object_name = 'articulo'

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Articulo, slug=slug_)