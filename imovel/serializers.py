from rest_framework import serializers
from .models import Propriedade


class PropriedadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Propriedade
        geo_field = 'point'
        fields = (
            'id',
            'nome',
            'valor',
            'tipo',
            'foto',
            'regiao',
            'posicao',
            'criado_em',
            'modificado_em',
        )
