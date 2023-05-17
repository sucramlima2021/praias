
from praias.models import Praias, Relatorios
import datetime
from praias.atualizacao import *
from rest_framework import viewsets
from praias.serializers import PraiaSerializer
from django.utils import timezone

# Create your views here.

class Lista_praias(viewsets.ReadOnlyModelViewSet):
    #verifica a ultima atualizacao dos relatorios
   
    rel = Relatorios.objects.all()

    for r in rel:
        at = r.verifica
        if at != timezone.now().date():
            if atualiza():
                if atualiza2():
                    if atualiza3():
                        pass
    queryset = Praias.objects.all()
    serializer_class = PraiaSerializer
   