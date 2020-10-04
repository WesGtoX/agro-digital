from import_export.resources import ModelResource
from .models import Tipo, Propriedade


class TipoResource(ModelResource):

    class Meta:
        model = Tipo


class PropriedadeResource(ModelResource):

    class Meta:
        model = Propriedade
        exclude = ('foto',)
