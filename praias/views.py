from django.http import JsonResponse, HttpResponse
from praias.models import Praias, Relatorios
from django.core import serializers
import datetime
from praias.atualizacao import *
# Create your views here.

def lista_praias(request):
    #verifica a ultima atualizacao dos relatorios
    at = Relatorios.objects.all()[0].verifica
    if at != datetime.date.today():
        if atualiza():
            if atualiza2():
                if atualiza3():
                    print('atualização concluida')
    #retorna um objeto json com a listagem das praias
    praias = serializers.serialize('json', Praias.objects.all())
    return JsonResponse(praias, safe=False)

def ini(request):
     #verifica a ultima atualizacao dos relatorios
    at = Relatorios.objects.all()[0].verifica
    if at != datetime.date.today():
        if atualiza():
            if atualiza2():
                if atualiza3():
                    print('atualização concluida')
    
    
    return HttpResponse('<h1>Balneabilidade das praias do Rio de Janeiro.</h1>')

