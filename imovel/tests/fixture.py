import factory
from faker import Faker
from imovel.models import Propriedade

fake = Faker(['pt_BR'])


coordinates = [
    'POINT(-21.20634 -47.80432)',
    'POINT(-21.19656 -47.80977)',
    'POINT(-21.13604 -48.00545)',
    'POINT(-21.1359 -48.0051)'
]


class PropriedadeFactory(factory.django.DjangoModelFactory):
    """Fixture para cadastrar uma Propriedade"""

    class Meta:
        model = Propriedade

    nome = factory.Faker('company')
    valor = factory.Faker('pyfloat', right_digits=2, positive=True, min_value=None, max_value=9999999)
    posicao = fake.word(ext_word_list=coordinates)
