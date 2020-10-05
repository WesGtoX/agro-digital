from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from .fixture import PropriedadeFactory
from imovel.models import Tipo

User = get_user_model()


class PropriedadeViewSetTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='bruce', email='bruce@wayne.com', password='imbatman'
        )
        self.anon_user = User.objects.create_user(
            username='jane', email='jane@joe.com', password='imnoone'
        )

        self.unath_client = APIClient()

        self.client = APIClient()
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        self.tipo = Tipo.objects.create(id=1, nome='Terreno')

    def test_perform_create(self):
        response = self.client.post(reverse('propriedade-list'), data={})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list(self):
        PropriedadeFactory.create_batch(5, tipo=self.tipo, posicao='POINT(-21.20634 -47.80432)')

        response = self.unath_client.get(reverse('propriedade-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('propriedade-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 1)

    def test_list_field_dist_point(self):
        PropriedadeFactory.create_batch(2, tipo=self.tipo, posicao='POINT(-21.20634 -47.80432)')
        PropriedadeFactory.create_batch(3, tipo=self.tipo, posicao='POINT(-21.13625 -48.00624)')

        response = self.client.get(f'{reverse("propriedade-list")}{"?dist=2000&point=-21.13625,-48.00624"}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 3)

    def test_retrieve(self):
        propriedade = PropriedadeFactory.create(id=10, tipo=self.tipo)

        response = self.unath_client.get(reverse('propriedade-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('propriedade-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], propriedade.nome)
        self.assertEqual(float(response.data['valor']), float(propriedade.valor))

    def test_update(self):
        PropriedadeFactory.create(id=21, tipo=self.tipo)
        response = self.client.put(reverse('propriedade-detail', args=[21]), data={})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update(self):
        PropriedadeFactory.create(id=22, tipo=self.tipo)
        response = self.client.patch(reverse('propriedade-detail', args=[22]), data={})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_destroy(self):
        PropriedadeFactory.create(id=15, tipo=self.tipo)
        response = self.client.delete(reverse('propriedade-detail', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
