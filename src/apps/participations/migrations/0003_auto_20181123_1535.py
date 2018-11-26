# Generated by Django 2.1.3 on 2018-11-23 17:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('participations', '0002_auto_20181121_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opinionvote',
            name='excerpt',
        ),
        migrations.AlterUniqueTogether(
            name='opinionvote',
            unique_together={('suggestion', 'owner')},
        ),
    ]