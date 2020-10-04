from django.db import models


class Regiao(models.Model):
    slug = models.SlugField('Slug', unique=True)
    nome = models.CharField('Nome', max_length=50)
    estado = models.CharField('Estado', max_length=50)

    def __str__(self):
        return f'Região: {self.nome}, Estado: {self.estado}'

    class Meta:
        verbose_name = 'Região'
        verbose_name_plural = 'Regiões'
        ordering = ['id', 'nome']


class Cidade(models.Model):
    slug = models.SlugField('Slug', unique=True)
    nome = models.CharField('Nome', max_length=50)
    regiao = models.ForeignKey(
        Regiao, verbose_name='Região',
        related_name='cidade',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Cidade: {self.nome}, Estado: {self.get_estado()}, Região: {self.get_regiao()}'

    def get_regiao(self):
        return self.regiao.nome

    def get_estado(self):
        return self.regiao.estado

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['id', 'nome']
