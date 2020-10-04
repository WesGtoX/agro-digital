# Generated by Django 3.1.1 on 2020-10-04 01:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imovel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propriedade',
            options={'verbose_name': 'Propriedade', 'verbose_name_plural': 'Propriedades'},
        ),
        migrations.AlterModelOptions(
            name='tipo',
            options={'verbose_name': 'Tipo', 'verbose_name_plural': 'Tipos'},
        ),
        migrations.AddField(
            model_name='propriedade',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propriedade',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em'),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='propriedade', to='imovel.tipo', verbose_name='Tipo'),
        ),
    ]