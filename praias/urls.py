
from django.urls import path, include
from praias.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', Lista_praias)

urlpatterns = [
    path('', include(router.urls)),
   
    #url para rodar a rotina de atualização manualmente
    #path('at/', at, name='atualiza'),
    
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )