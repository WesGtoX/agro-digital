from django.contrib import admin
from .models import Regiao, Cidade


@admin.register(Regiao)
class RegiaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'estado']
    list_filter = ['estado']
    search_fields = ['nome', 'estado', 'slug']
    prepopulated_fields = {'slug': ('nome', 'estado')}


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'regiao']
    list_filter = ['regiao']
    search_fields = ['nome', 'regiao', 'slug']
    prepopulated_fields = {'slug': ('nome',)}
