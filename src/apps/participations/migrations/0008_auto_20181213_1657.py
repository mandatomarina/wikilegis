# Generated by Django 2.1.4 on 2018-12-13 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participations', '0007_merge_20181129_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suggestion',
            options={'ordering': ('start_index',), 'verbose_name': 'suggestion', 'verbose_name_plural': 'suggestions'},
        ),
    ]