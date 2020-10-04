from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import migrations


def forward(apps, schema_editor):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(username='admin', password='adminadmin')


def reverte(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(forward, reverte),
    ]
