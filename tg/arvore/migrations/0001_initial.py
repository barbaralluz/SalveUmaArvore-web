# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arvore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.CharField(max_length=100, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=100, verbose_name='Longitude')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('tipo_arvore', models.CharField(max_length=20, verbose_name='Tipo de Arvore')),
                ('altura', models.CharField(max_length=125, verbose_name='Altura')),
                ('diametro', models.CharField(max_length=255, null=True, verbose_name='Diametro', blank=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
