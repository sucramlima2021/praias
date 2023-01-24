
from django.urls import path
from praias.views import lista_praias, ini
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ini, name = 'ini'),
    path('lista/', lista_praias, name='lista_praias'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )