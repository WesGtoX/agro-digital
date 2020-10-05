from rest_framework import viewsets
from rest_framework_gis.filters import (
    DistanceToPointFilter, DistanceToPointOrderingFilter
)

from .models import Propriedade
from .serializers import PropriedadeSerializer


class PropriedadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer
    filter_backends = (DistanceToPointOrderingFilter, DistanceToPointFilter)
    distance_filter_field = 'posicao'
    distance_filter_convert_meters = True
    distance_filter_add_distance = True
