# coding: utf-8

from django import forms

from tg.core.models  import Tree
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TreeForm(forms.ModelForm):
    foto1 = forms.ImageField(label='Adicione Fotos')
    foto2 = forms.ImageField(label='')
    
    class Meta:
        model = Tree
        fields = ("longitude", "latitude", "especie", "altura", "diametro", "informacoes_adicionais",
        	"foto1", "foto2")


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
