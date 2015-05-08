# coding: utf-8

from django import forms

from tg.core.models  import Tree
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TreeForm(forms.ModelForm):
    foto1 = forms.ImageField(label='Adicione Fotos', required=False)
    foto2 = forms.ImageField(label='', required=False)
    
    class Meta:
        model = Tree
        fields = ("longitude", "latitude", "especie", "altura", "diametro", "informacoes_adicionais",
        	"foto1", "foto2")


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    

    class Meta:
        model = User
        fields = ("username", "email")

    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', "password2"]:
            self.fields[fieldname].help_text = None
