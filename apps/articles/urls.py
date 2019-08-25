from django.contrib import admin
from django.urls import path, include
from .views import ArticuloVista, ArticuloDetalleVista
from . import views


urlpatterns = [
    path('labs/', ArticuloVista.as_view(), name='articulos'),
    path('labs/<slug>/', ArticuloDetalleVista.as_view(), name='articulo-detalle')
]
