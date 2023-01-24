from django.http import JsonResponse, HttpResponse
from praias.models import Praias
from django.core import serializers
# Create your views here.

def lista_praias(request):
    #retorna um objeto json com a listagem das praias
    praias = serializers.serialize('json', Praias.objects.all())
    return JsonResponse(praias, safe=False)

def ini(request):
   
    return HttpResponse('<h1>Balneabilidade das praias do Rio de Janeiro.</h1>')

