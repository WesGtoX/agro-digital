from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class Propriedade(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(decimal_places=2, max_digits=12)
    tipo = models.ForeignKey(
        Tipo, verbose_name='Tipo',
        related_name='propriedade',
        on_delete=models.PROTECT
    )
    foto = models.FileField()

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Propriedade'
        verbose_name_plural = 'Propriedades'
