from django.test import TestCase
from localizacao.models import Regiao, Cidade


class RegiaoModelTestCase(TestCase):

    def test_create_regiao(self):
        regiao = Regiao.objects.create(
            nome='Centro Oeste',
            estado='Comics'
        )
        self.assertEqual(regiao.nome, 'Centro Oeste')
        self.assertEqual(regiao.estado, 'Comics')
        self.assertIn('Centro Oeste', str(regiao))


class CidadeModelTestCase(TestCase):

    def setUp(self):
        self.regiao = Regiao.objects.create(
            nome='Sudeste',
            estado='Nova Jersey'
        )

    def test_create_cidade(self):
        cidade = Cidade.objects.create(
            nome='Gotham',
            regiao=self.regiao,
        )
        self.assertEqual(cidade.nome, 'Gotham')
        self.assertEqual(cidade.get_regiao(), self.regiao.nome)
        self.assertEqual(cidade.get_estado(), self.regiao.estado)
        self.assertIn('Cidade: Gotham', str(cidade))
