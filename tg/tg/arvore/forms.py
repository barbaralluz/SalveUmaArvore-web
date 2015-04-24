# coding: utf-8

from django import forms

from tg.arvore.models  import Arvore
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormArvore(forms.ModelForm):

    class Meta:
        model = Arvore
        fields = ("latitude", "longitude", "nome", "tipo_arvore", "altura", "diametro")


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")
