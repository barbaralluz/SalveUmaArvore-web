# coding: utf-8

from django.contrib import admin
from tg.core.models import Tree, Profile
from municipios.models import UF, Municipio

admin.site.register(Tree)
admin.site.register(Profile)
admin.site.register(Municipio)
admin.site.register(UF)
