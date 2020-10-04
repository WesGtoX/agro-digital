from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from .fixture import RegiaoFactory, CidadeFactory

User = get_user_model()


class CidadeViewSetTests(APITestCase):

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

        self.regiao = RegiaoFactory.create(id=1)

    def test_perform_create(self):
        data = {
            'nome': 'Gotham',
            'regiao': self.regiao.id
        }
        response = self.unath_client.post(reverse('cidade-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post(reverse('cidade-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], data['nome'])
        self.assertEqual(response.data['slug'], 'gotham')

    def test_list(self):
        CidadeFactory.create_batch(5, regiao=self.regiao)

        response = self.unath_client.get(reverse('cidade-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('cidade-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 5)

    def test_retrieve(self):
        cidade = CidadeFactory.create(id=10, regiao=self.regiao)

        response = self.unath_client.get(reverse('cidade-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('cidade-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], cidade.nome)

    def test_update(self):
        cidade = CidadeFactory.create(id=21, regiao=self.regiao)
        data = {'nome': 'Gotham City', 'regiao': self.regiao.id}
        self.assertNotEqual(cidade.nome, data['nome'])

        response = self.unath_client.put(reverse('cidade-detail', args=[21]), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(reverse('cidade-detail', args=[21]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], data['nome'])
        self.assertEqual(response.data['slug'], 'gotham-city')

    def test_partial_update(self):
        cidade = CidadeFactory.create(id=22, regiao=self.regiao)
        data = {'nome': 'Gotham City'}
        self.assertNotEqual(cidade.nome, data['nome'])

        response = self.unath_client.patch(reverse('cidade-detail', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.patch(reverse('cidade-detail', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], data['nome'])

    def test_destroy(self):
        CidadeFactory.create(id=15, regiao=self.regiao)
        response = self.unath_client.get(reverse('cidade-detail', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('cidade-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 1)

        response = self.client.delete(reverse('cidade-detail', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(reverse('cidade-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
