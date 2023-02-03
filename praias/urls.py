
from django.urls import path
from praias.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ini, name = 'ini'),
    path('lista/', lista_praias, name='lista_praias'),
    #url para rodar a rotina de atualização manualmente
    #path('at/', at, name='atualiza'),
    
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )