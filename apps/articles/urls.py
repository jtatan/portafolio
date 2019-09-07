from django.contrib import admin
from django.urls import path, include
from .views import ArticuloListaVista, ArticuloDetalleVista, CategoriaListaVista, CategoriaDetalleListaVista
from . import views


urlpatterns = [
    path('labs/', ArticuloListaVista.as_view(), name='lista'),
    path('labs/<slug>/', ArticuloDetalleVista.as_view(), name='detalle'),
    path('categorias/', CategoriaListaVista.as_view(), name='categoria-lista'),
    path('categorias/<slug>/', CategoriaDetalleListaVista.as_view(), name='categoria-detalle')
]
