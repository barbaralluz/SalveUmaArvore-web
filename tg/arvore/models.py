from django.db import models
from django.contrib.auth.models import User

# coding: utf-8

class Arvore(models.Model):
    latitude = models.CharField(verbose_name=u'Latitude', max_length=100)
    longitude = models.CharField(verbose_name=u'Longitude', max_length=100)
    nome = models.CharField(verbose_name=u'Nome', max_length=100)
    tipo_arvore = models.CharField(verbose_name=u'Tipo de Arvore', max_length=20)
    altura = models.CharField(u'Altura', max_length=125)
    diametro = models.CharField(u'Diametro', max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
    	return u"Nome: %s " % (
                self.nome)
