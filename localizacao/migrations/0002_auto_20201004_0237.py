# Generated by Django 3.1.1 on 2020-10-04 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiao',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug'),
        ),
    ]