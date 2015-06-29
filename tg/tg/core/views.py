# coding: utf-8

from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy, reverse

from tg.core.models import Tree, User, Profile
from tg.core.forms import TreeForm, UserForm, ProfileForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, render_to_response, get_object_or_404, redirect


index = TemplateView.as_view(template_name='index.html')

# Autenticação e Cadastro de Usuário
def signin(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid(): 
            form.save()  
            return redirect(log_in) 
        else:
            return render(request, "signin.html", {"form": form})
    return render(request, "signin.html", {"form": UserForm() })

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():
           login(request, form.get_user())
           return redirect(control_panel) 
        else:
            return render(request, "login.html", {"form": form})
    return render(request, "login.html", {"form": AuthenticationForm()})

#Perfil
@login_required
def profile(request, username):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(control_panel)
    else:
        form = ProfileForm(instance=user)
    return render_to_response("profile.html", {'form':form},
            context_instance=RequestContext(request))

#Painel de Controle
@login_required
def control_panel(request):
    return ListView.as_view(
        queryset = Tree.objects.all(),
        template_name='control_panel.html')(request)

#Visualizar Mapa do Usuário
@login_required
def user_map(request, username):
    return ListView.as_view(
        queryset = Tree.objects.filter(usuario=request.user),
        template_name='map.html')(request)

#Visualizar Mapa com Todas as Árvores
def map(request):
    return ListView.as_view(
        queryset = Tree.objects.all(),
        template_name='map.html')(request)

#CRUD Árvores
@login_required
def tree_create(request):
    if request.method == 'POST': 
        form = TreeForm(request.POST, request.FILES)
        if form.is_valid():
            tree = form.save(commit=False)
            tree.usuario = request.user
            tree.save()
            return redirect(tree_list)
    else:
        form = TreeForm()
    return render_to_response("tree_form.html", {'form': form},
            context_instance=RequestContext(request))

#Lista com Todas as Árvores
@login_required
def tree_list(request):
    return ListView.as_view(
        queryset = Tree.objects.all(),
        template_name='tree_list.html')(request)

#Lista de Árvores do Usuário
@login_required
def user_tree_list(request, username):
    return ListView.as_view(
        queryset = Tree.objects.filter(usuario=request.user),
        paginate_by=20,
        template_name='user_tree_list.html')(request)

@login_required
def tree_update(request, nr_tree):
    tree = get_object_or_404(Tree, usuario=request.user, id=nr_tree)
    if request.method == "POST":
        form = TreeForm(request.POST, request.FILES, instance=tree)
        if form.is_valid():
            form.save()
            return redirect(tree_list)
    else:
        form = TreeForm(instance=tree)
    return render_to_response("tree_form.html", {'form':form},
            context_instance=RequestContext(request))

@login_required
def tree_delete(request, nr_tree):
    tree = get_object_or_404(Tree, usuario=request.user, id=nr_tree)
    if request.method == "POST":
        
        tree.delete()
        return redirect(tree_list)
    return render_to_response("confirm_delete_tree.html", {'object': tree},
                context_instance=RequestContext(request))