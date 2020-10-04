from django.contrib import admin
from .models import Tipo, Propriedade


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
    search_fields = ['nome']


@admin.register(Propriedade)
class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo']
    list_filter = ['nome', 'tipo']
    search_fields = ['nome']
