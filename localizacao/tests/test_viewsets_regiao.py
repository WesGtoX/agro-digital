from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from .fixture import RegiaoFactory

User = get_user_model()


class RegiaoViewSetTests(APITestCase):

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

    def test_perform_create(self):
        data = {
            'nome': 'Centro Oeste',
            'estado': 'Comics',
        }
        response = self.unath_client.post(reverse('regiao-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post(reverse('regiao-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], data['nome'])
        self.assertEqual(response.data['estado'], data['estado'])
        self.assertEqual(response.data['slug'], 'centro-oeste-comics')

    def test_list(self):
        RegiaoFactory.create_batch(5)

        response = self.unath_client.get(reverse('regiao-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('regiao-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 5)

    def test_retrieve(self):
        regiao = RegiaoFactory.create(id=10)

        response = self.unath_client.get(reverse('regiao-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('regiao-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], regiao.nome)

    def test_update(self):
        regiao = RegiaoFactory.create(id=21)
        data = {'nome': 'Sudeste', 'estado': 'Cave'}
        self.assertNotEqual(regiao.nome, data['nome'])

        response = self.unath_client.put(reverse('regiao-detail', args=[21]), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(reverse('regiao-detail', args=[21]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], data['nome'])
        self.assertEqual(response.data['estado'], data['estado'])
        self.assertEqual(response.data['slug'], 'sudeste-cave')

    def test_partial_update(self):
        regiao = RegiaoFactory.create(id=22)
        data = {'nome': 'Nordeste'}
        self.assertNotEqual(regiao.nome, data['nome'])

        response = self.unath_client.patch(reverse('regiao-detail', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.patch(reverse('regiao-detail', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], data['nome'])

    def test_destroy(self):
        RegiaoFactory.create(id=15)
        response = self.unath_client.get(reverse('regiao-detail', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('regiao-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 1)

        response = self.client.delete(reverse('regiao-detail', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(reverse('regiao-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
