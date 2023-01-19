
from django.urls import path
from praias.views import lista_praias
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('lista/', lista_praias, name='lista_praias'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )