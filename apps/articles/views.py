from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Articulo, Categoria

# ----- Artículos ----- #
class ArticuloListaVista(ListView):
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

# ----- Categorías ----- #

class CategoriaListaVista(ListView):
    model = Categoria
    template_name = 'labs/categorias/lista.html'
    context_object_name = 'categorias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoriaDetalleListaVista(DetailView):
    template_name = 'labs/categorias/detalle.html'
    queryset = Categoria.objects.all()
    context_object_name = 'categoria'

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Categoria, slug=slug_)

    def get_context_data(self, **kwargs):
        context = super(CategoriaDetalleListaVista, self).get_context_data(**kwargs)
        context['articulos'] = Articulo.objects.filter(categorias=self.get_object())
        return context