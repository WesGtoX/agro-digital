from django.test import TestCase
from imovel.models import Tipo, Propriedade
from localizacao.models import Regiao


class TipoModelTestCase(TestCase):

    def test_create_tipo(self):
        tipo = Tipo.objects.create(nome='Terreno')
        self.assertEqual(tipo.nome, 'Terreno')
        self.assertEqual(str(tipo), 'Terreno')


class PropriedadeModelTestCase(TestCase):

    def setUp(self):
        self.tipo = Tipo.objects.create(nome='Casa')
        self.regiao = Regiao.objects.create(
            nome='Centro Oeste',
            estado='Sampa'
        )

    def test_create_propriedade(self):
        propriedade = Propriedade.objects.create(
            nome='Mansao Wayne',
            valor=150000.00,
            tipo=self.tipo,
            regiao=self.regiao,
        )
        self.assertEqual(propriedade.nome, 'Mansao Wayne')
        self.assertEqual(propriedade.get_tipo(), self.tipo.nome)
        self.assertEqual(propriedade.get_regiao(), self.regiao.nome)
        self.assertIn('Propriedade: Mansao Wayne', str(propriedade))
