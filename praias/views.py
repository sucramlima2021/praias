
from praias.models import Praias, Relatorios
import datetime
from praias.atualizacao import *
from rest_framework import viewsets
from praias.serializers import PraiaSerializer
# Create your views here.

class Lista_praias(viewsets.ModelViewSet):
    #verifica a ultima atualizacao dos relatorios
    at = Relatorios.objects.all()[0].verifica
    if at != datetime.date.today():
        if atualiza():
            if atualiza2():
                if atualiza3():
                    pass
    queryset = Praias.objects.all()
    serializer_class = PraiaSerializer
   