from rest_framework import viewsets

from slugify import slugify

from .models import Regiao, Cidade
from .serializers import RegiaoSerializer, CidadeSerializer


class RegiaoViewSet(viewsets.ModelViewSet):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer

    def perform_create(self, serializer):
        nome = serializer.validated_data.get('nome', '')
        estado = serializer.validated_data.get('estado', '')
        serializer.save(slug=slugify(f'{nome} {estado}'))

    def perform_update(self, serializer):
        nome = serializer.validated_data.get('nome', '')
        estado = serializer.validated_data.get('estado', '')
        serializer.save(slug=slugify(f'{nome} {estado}'))


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

    def perform_create(self, serializer):
        nome = serializer.validated_data.get('nome', '')
        serializer.save(slug=slugify(nome))

    def perform_update(self, serializer):
        nome = serializer.validated_data.get('nome', '')
        serializer.save(slug=slugify(nome))
