# Generated by Django 3.0.2 on 2020-08-19 20:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sugestoes', '0003_projeto_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='apoiador',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
