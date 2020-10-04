from django.test import TestCase
from imovel.models import Tipo, Propriedade


class TipoModelTestCase(TestCase):

    def test_create_tipo(self):
        tipo = Tipo.objects.create(nome='Terreno')
        self.assertEqual(tipo.nome, 'Terreno')
        self.assertEqual(str(tipo), 'Terreno')


class PropriedadeModelTestCase(TestCase):

    def setUp(self):
        self.tipo = Tipo.objects.create(nome='Casa')

    def test_create_propriedade(self):
        propriedade = Propriedade.objects.create(
            nome='Mansao Wayne',
            valor=150000.00,
            tipo=self.tipo,
        )
        self.assertEqual(propriedade.nome, 'Mansao Wayne')
        self.assertEqual(str(propriedade.tipo), self.tipo.nome)
        self.assertEqual(str(propriedade), 'Mansao Wayne')
