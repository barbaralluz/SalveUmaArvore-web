# coding: utf-8

from django import forms
from tg.core.models  import Tree, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from municipios.models import UF, Municipio

from municipios.widgets import SelectMunicipioWidget
    
# Busca por estado, cidade, bairro, endereço, espécie
# deixar opção para marcar Minhas Árvores
class SearchTreeForm(forms.Form):

    municipio = forms.IntegerField(label=u"UF - Município", widget=SelectMunicipioWidget,  required=False)
    bairro = forms.CharField(label=u"Bairro", required=False)
    endereco = forms.CharField(label=u"Endereço", required=False)
    especie = forms.CharField(label=u"Espécie", required=False)
    minhas_arvores = forms.BooleanField(label=u"Minhas Árvores", required=False)
    todas_arvores = forms.BooleanField(label=u"Todas as Árvores", required=False, initial='True')
    user = forms.CharField(label=u"Usuário", required=False)
    
    def __init__(self, *args, **kwargs):
        self.queryset = kwargs.pop('queryset', Tree.objects.all())
        super(SearchTreeForm, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.is_valid():
            trees = self.queryset
            minhas_arvores = self.cleaned_data.get('minhas_arvores', False)
            user = self.cleaned_data.get('user', False)
            if minhas_arvores:
                trees = trees.filter(usuario=user)
            municipio_uf = self.cleaned_data.get('municipio_uf', False)
            if municipio_uf:
                trees = trees.filter(administrative_area_level_1=municipio_uf)
            municipio = self.cleaned_data.get('municipio', False)
            if municipio:
                trees = trees.filter(locality=municipio)
            bairro = self.cleaned_data.get('bairro', False)
            if bairro:
                trees = trees.filter(neighborhood=bairro)
            endereco = self.cleaned_data.get('endereco', False)
            if endereco:
                trees = trees.filter(route=endereco)
            especie = self.cleaned_data.get('especie', False)
            if especie:
                trees = trees.filter(especie=especie)
            return trees
        else:
            return self.queryset

class TreeForm(forms.ModelForm):
    foto = forms.ImageField(label="Adicione uma foto", required=False)
    administrative_area_level_1 = forms.ModelChoiceField(queryset=UF.objects.all(), label="Estado")
    locality = forms.ModelChoiceField(queryset=Municipio.objects.all(), label="Municipio")
    class Meta:
        model = Tree
        fields = ("geometry", "country", "administrative_area_level_1",
                  "locality", "neighborhood", "route", 
                  "numero", "postal_code", "point_of_interest",
                  "condicao_arvore", "especie", "altura", "condicao_raiz", 
                  "condicao_luz", "condicao_man", "descricao", "foto1", "foto2", "foto3")

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