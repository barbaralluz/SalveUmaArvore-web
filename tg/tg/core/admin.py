# coding: utf-8

from django.contrib import admin
from tg.core.models import Tree, Profile
from municipios.models import UF, Municipio
from fluent_comments.models import FluentComment
from django_comments.models import Comment

admin.site.register(Tree)
admin.site.register(Profile)
admin.site.register(Municipio)
admin.site.register(UF)
admin.site.register(FluentComment)
admin.site.register(Comment)