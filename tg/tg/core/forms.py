# coding: utf-8

from django import forms

from tg.core.models  import Tree, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TreeForm(forms.ModelForm):
    foto = forms.ImageField(label="Adicione uma foto", required=False)
    class Meta:
        model = Tree
        fields = ("geometry", "country", "administrative_area_level_1", 
                  "locality", "neighborhood", "route", 
                  "numero", "postal_code", "point_of_interest",
                  "especie", "altura", "diametro", "informacoes_adicionais", "foto")

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', "password2"]:
            self.fields[fieldname].help_text = None

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None