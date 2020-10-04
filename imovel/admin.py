from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Tipo, Propriedade
from .resources import TipoResource, PropriedadeResource


@admin.register(Tipo)
class TipoAdmin(ImportExportModelAdmin):
    resource_class = TipoResource
    list_display = ['nome']
    list_filter = ['nome']
    search_fields = ['nome']


@admin.register(Propriedade)
class PropriedadeAdmin(ImportExportModelAdmin):
    resource_class = PropriedadeResource
    list_display = ['nome', 'tipo']
    list_filter = ['nome', 'tipo']
    search_fields = ['nome']
