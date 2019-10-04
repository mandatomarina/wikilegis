# Generated by Django 2.2.5 on 2019-09-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='elector',
            field=models.BooleanField(blank=True, default=0, verbose_name='elector'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='mobile'),
        ),
    ]