# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Tree(models.Model):
    longitude = models.CharField(verbose_name=u'Longitude', max_length=100)
    latitude = models.CharField(verbose_name=u'Latitude', max_length=100)
    especie = models.CharField(verbose_name=u'Espécie', max_length=200)
    altura = models.CharField(u'Altura', max_length=100)
    diametro = models.CharField(u'Diâmetro', max_length=100)
    informacoes_adicionais = models.TextField(u'Informações Adicionais', null=True, blank=True)
    data_cadastro = models.DateField(default=datetime.now)  
    foto1 = models.ImageField(upload_to='tg/core/static/img/trees', null=True, blank=True)
    foto2 = models.ImageField(upload_to='tg/core/static/img/trees', null=True, blank=True)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return u"Código: %d " % (
            self.id)