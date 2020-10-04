import factory
from faker import Faker
from localizacao.models import Regiao, Cidade

fake = Faker(['pt_BR'])


class RegiaoFactory(factory.django.DjangoModelFactory):
    """Fixture para cadastrar uma Região"""

    class Meta:
        model = Regiao

    nome = factory.Faker('country')
    estado = factory.Faker('city')


class CidadeFactory(factory.django.DjangoModelFactory):
    """Fixture para cadastrar uma Cidade"""

    class Meta:
        model = Cidade

    nome = factory.Faker('city')
