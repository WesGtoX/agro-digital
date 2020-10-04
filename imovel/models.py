from django.db import models
from localizacao.models import Regiao


class Tipo(models.Model):
    nome = models.CharField('Nome', max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class Propriedade(models.Model):
    nome = models.CharField('Nome', max_length=50)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=12)
    tipo = models.ForeignKey(
        Tipo, verbose_name='Tipo',
        related_name='propriedade_tipo',
        on_delete=models.PROTECT
    )
    foto = models.FileField()

    regiao = models.ForeignKey(
        Regiao, verbose_name='Região',
        related_name='propriedade_regiao',
        on_delete=models.PROTECT,
        blank=True, null=True
    )

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return f'Propriedade: {self.nome}, Tipo: {self.tipo.nome}, Região: {self.get_regiao()}'

    def get_tipo(self):
        return self.tipo.nome

    def get_regiao(self):
        return self.regiao.nome

    class Meta:
        verbose_name = 'Propriedade'
        verbose_name_plural = 'Propriedades'
