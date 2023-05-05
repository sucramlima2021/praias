from .models import Praias
from rest_framework import serializers


class PraiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Praias
        fields = ['nome', 'bairro', 'coord', 'mapa', 'propria', 'atualizado_em']

 