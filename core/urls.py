from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('', include('apps.articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

