# Generated by Django 2.1.5 on 2019-02-13 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20190128_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentAuthorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_id', models.PositiveIntegerField(default=0, verbose_name='CD ID')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='image url')),
                ('party_initials', models.CharField(blank=True, max_length=250, null=True, verbose_name='party initials')),
                ('uf', models.CharField(blank=True, max_length=250, null=True, verbose_name='uf')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='infos', to='projects.DocumentAuthor', verbose_name='author')),
            ],
            options={
                'verbose_name': 'Author Information',
                'verbose_name_plural': 'Authors Informations',
            },
        ),
    ]