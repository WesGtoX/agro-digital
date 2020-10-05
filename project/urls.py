from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .viewsets import UsuarioViewSet
from imovel.viewsets import PropriedadeViewSet
from localizacao.viewsets import RegiaoViewSet, CidadeViewSet

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('propriedades', PropriedadeViewSet)
router.register('regioes', RegiaoViewSet)
router.register('cidades', CidadeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls')),
]
