from rest_framework import serializers
from .models import Regiao, Cidade


class RegiaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regiao
        fields = (
            'id',
            'slug',
            'nome',
            'estado',
        )


class CidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cidade
        fields = (
            'id',
            'slug',
            'nome',
            'regiao',
        )
