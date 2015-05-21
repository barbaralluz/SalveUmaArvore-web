# coding: utf-8

from django.contrib import admin
from tg.core.models import Map, Tree, Profile

admin.site.register(Tree)
admin.site.register(Profile)
admin.site.register(Map)