# coding: utf-8

from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy, reverse

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.comments import Comment

from django_user_agents.utils import get_user_agent
   
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from django.core.context_processors import csrf

from django.http import HttpResponse, HttpResponseBadRequest

from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter


from tg.core.models import Tree, User, Profile
from tg.core.forms import TreeForm, UserForm, ProfileForm, SearchTreeForm
from municipios.models import Municipio, UF
from tg.core.serializers import TreeSerializer, UserDetailsSerializer, LoginSerializer, TokenSerializer
from django.conf import settings

from django.contrib.auth import login, logout
from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView

def index(request):
    arvores = Tree.objects.all();

    if request.method == 'POST':
        form = SearchTreeForm(request.POST)
        if form.is_valid():
            condicao = form.cleaned_data['condicao']
            if condicao:
                arvores = arvores.filter(condicao_arvore=condicao)
            
            manutencao = form.cleaned_data['man']
            if manutencao:
                arvores = arvores.filter(condicao_man=manutencao)
            
            luz = form.cleaned_data['luz']
            if luz:
                arvores = arvores.filter(condicao_luz=luz)

            raiz = form.cleaned_data['raiz']
            if raiz:
                arvores = arvores.filter(condicao_raiz=raiz)
    else:
        form = SearchTreeForm()
    return render(request, 'index.html', {'search_form': form, 'arvores': arvores})

# Autenticação e Cadastro de Usuário
def signin(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid(): 
            form.save()  
            return redirect(log_in) 
        else:
            if get_user_agent(request).is_mobile | get_user_agent(request).is_tablet:
                return render(request, "signin_mob.html", {"form": form})
            else:
                return render(request, "signin.html", {"form": form})
    if get_user_agent(request).is_mobile | get_user_agent(request).is_tablet:
        return render(request, "signin_mob.html", {"form": UserForm() })
    else:  
        return render(request, "signin.html", {"form": UserForm() })

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():
           login(request, form.get_user())
           return redirect(index)
        else:
            if get_user_agent(request).is_mobile | get_user_agent(request).is_tablet:
                return render(request, "login_mob.html", {"form": form})
            else:
                return render(request, "login.html", {"form": form})
    if get_user_agent(request).is_mobile | get_user_agent(request).is_tablet:
        return render(request, "login_mob.html", {"form": AuthenticationForm()})
    else:
        return render(request, "login.html", {"form": AuthenticationForm()})

class StatisticsView(TemplateView):
    template_name = 'statistics.html'

    def get_context_data(self, **kwargs):
        context = super(StatisticsView, self).get_context_data(**kwargs)
        
        total_arvores = Tree.objects.all().count()

        cidades = []
        estados = []
        
        qtde_cidades = {}
        qtde_estados = {}
        
        if total_arvores != 0:

            for arvore in Tree.objects.all():

                cidades.append(arvore.locality)
                qtde_cidades = {i:cidades.count(i) for i in cidades}

                estados.append(arvore.administrative_area_level_1)
                qtde_estados = {i:estados.count(i) for i in estados}
            
            arvores_usuario = Tree.objects.filter(usuario=self.request.user).count()
            porcentagem_arvores_usuario = (arvores_usuario * 100) / total_arvores

            #arvores por condição
            arvores_boa = Tree.objects.filter(condicao_arvore='Boa - Sem sinal de praga, danos ou doenças').count()
            porcentagem_arvores_boa = (arvores_boa * 100) / total_arvores

            arvores_regular = Tree.objects.filter(condicao_arvore='Regular - Pequenos sinais de praga, danos ou doenças').count()
            porcentagem_arvores_regular = (arvores_regular * 100) / total_arvores

            arvores_ruim = Tree.objects.filter(condicao_arvore='Ruim - Risco de queda, sinal de forte ataque de pragas, doenças e danos').count()
            porcentagem_arvores_ruim = (arvores_ruim * 100) / total_arvores

            arvores_caidas = Tree.objects.filter(condicao_arvore='Caída - Árvore caída').count()
            porcentagem_arvores_caidas = (arvores_caidas * 100) / total_arvores

            #arvores por condicao de raíz
            arvores_raiz_sem = Tree.objects.filter(condicao_raiz='Não apresenta problemas - Raízes profundas e sem danos a edificações e pisos próximos').count()
            porcentagem_arvores_raiz_sem = (arvores_raiz_sem * 100) / total_arvores

            arvores_raiz_aponta = Tree.objects.filter(condicao_raiz='Aponta - Raízes superficiais, sem rachaduras, elevação ou desníveis').count()
            porcentagem_arvores_raiz_aponta = (arvores_raiz_aponta * 100) / total_arvores

            arvores_raiz_quebra = Tree.objects.filter(condicao_raiz='Quebra - Raízes  expostas, presença de algumas rachaduras').count()
            porcentagem_arvores_raiz_quebra = (arvores_raiz_quebra * 100) / total_arvores

            arvores_raiz_destroi = Tree.objects.filter(condicao_raiz='Destrói - Raízes expostas, destruição da calçada').count()
            porcentagem_arvores_raiz_destroi = (arvores_raiz_destroi * 100) / total_arvores

            #arvores por proximidade da rede elétrica
            arvores_luz_sconflito = Tree.objects.filter(condicao_luz='Presente sem conflito').count()
            porcentagem_arvores_luz_sconflito = (arvores_luz_sconflito * 100) / total_arvores

            arvores_luz_cconflito = Tree.objects.filter(condicao_luz='Presente com conflito').count()
            porcentagem_arvores_luz_cconflito = (arvores_luz_cconflito * 100) / total_arvores

            arvores_luz_ausente = Tree.objects.filter(condicao_luz='Ausente').count()
            porcentagem_arvores_luz_ausente = (arvores_luz_ausente * 100) / total_arvores

            #arvores por necessidade de manutenção
            arvores_man_sem = Tree.objects.filter(condicao_man='Sem necessidade').count()
            porcentagem_arvores_man_sem = (arvores_man_sem * 100) / total_arvores

            arvores_man_afastar = Tree.objects.filter(condicao_man='Afastar de construções').count()
            porcentagem_arvores_man_afastar = (arvores_man_afastar * 100) / total_arvores

            arvores_man_luz = Tree.objects.filter(condicao_man='Liberar Rede Elétrica').count()
            porcentagem_arvores_man_luz = (arvores_man_luz * 100) / total_arvores

            arvores_man_copa = Tree.objects.filter(condicao_man='Levantamento de copa').count()
            porcentagem_arvores_man_copa = (arvores_man_copa * 100) / total_arvores    
        else:
            arvores_usuario = 0
            porcentagem_arvores_usuario = 0

            #arvores por condição
            arvores_boa = 0
            porcentagem_arvores_boa = 0

            arvores_regular = 0
            porcentagem_arvores_regular = 0

            arvores_ruim = 0
            porcentagem_arvores_ruim = 0

            arvores_caidas = 0
            porcentagem_arvores_caidas = 0

            #arvores por condicao de raíz
            arvores_raiz_sem = 0
            porcentagem_arvores_raiz_sem = 0

            arvores_raiz_aponta = 0
            porcentagem_arvores_raiz_aponta = 0

            arvores_raiz_quebra = 0
            porcentagem_arvores_raiz_quebra = 0

            arvores_raiz_destroi = 0
            porcentagem_arvores_raiz_destroi = 0

            #arvores por proximidade da rede elétrica
            arvores_luz_sconflito = 0
            porcentagem_arvores_luz_sconflito = 0

            arvores_luz_cconflito = 0
            porcentagem_arvores_luz_cconflito = 0

            arvores_luz_ausente = 0
            porcentagem_arvores_luz_ausente = 0

            #arvores por necessidade de manutenção
            arvores_man_sem = 0
            porcentagem_arvores_man_sem = 0

            arvores_man_afastar = 0
            porcentagem_arvores_man_afastar = 0

            arvores_man_luz = 0
            porcentagem_arvores_man_luz = 0

            arvores_man_copa = 0
            porcentagem_arvores_man_copa = 0           

        context.update({
            'total_arvores': total_arvores,
            'arvores_usuario':arvores_usuario,
            'porcentagem_arvores_usuario':porcentagem_arvores_usuario,

            'qtde_cidades': qtde_cidades,
            'qtde_estados': qtde_estados,

            'arvores_boa':arvores_boa,
            'porcentagem_arvores_boa':porcentagem_arvores_boa,
            'arvores_regular':arvores_regular,
            'porcentagem_arvores_regular':porcentagem_arvores_regular,
            'arvores_ruim':arvores_ruim,
            'porcentagem_arvores_ruim':porcentagem_arvores_ruim,
            'arvores_caidas':arvores_caidas,
            'porcentagem_arvores_caidas':porcentagem_arvores_caidas,

            'arvores_raiz_sem': arvores_raiz_sem,
            'porcentagem_arvores_raiz_sem': porcentagem_arvores_raiz_sem,
            'arvores_raiz_aponta': arvores_raiz_aponta,
            'porcentagem_arvores_raiz_aponta': porcentagem_arvores_raiz_aponta,
            'arvores_raiz_quebra': arvores_raiz_quebra,
            'porcentagem_arvores_raiz_quebra': porcentagem_arvores_raiz_quebra,
            'arvores_raiz_destroi': arvores_raiz_destroi,
            'porcentagem_arvores_raiz_destroi': porcentagem_arvores_raiz_destroi,

            'arvores_luz_ausente': arvores_luz_ausente,
            'porcentagem_arvores_luz_ausente': porcentagem_arvores_luz_ausente,
            'arvores_luz_sconflito': arvores_luz_sconflito,
            'porcentagem_arvores_luz_sconflito': porcentagem_arvores_luz_sconflito,
            'arvores_luz_cconflito': arvores_luz_cconflito,
            'porcentagem_arvores_luz_cconflito': porcentagem_arvores_luz_cconflito,
            
            'arvores_man_sem': arvores_man_sem,
            'porcentagem_arvores_man_sem': porcentagem_arvores_man_sem,
            'arvores_man_afastar': arvores_man_afastar,
            'porcentagem_arvores_man_afastar': porcentagem_arvores_man_afastar,
            'arvores_man_luz': arvores_man_luz,
            'porcentagem_arvores_man_luz': porcentagem_arvores_man_luz,
            'arvores_man_copa': arvores_man_copa,
            'porcentagem_arvores_man_copa': porcentagem_arvores_man_copa,
            
        })
        
        return context

statistics = StatisticsView.as_view()

#CRUD Árvores
@login_required
def tree_create(request):
    if request.method == 'POST': 
        form = TreeForm(request.POST, request.FILES)
        if form.is_valid():
            tree = form.save(commit=False)
            tree.usuario = request.user
            tree.save()
            return redirect('user_tree_list', username=request.user.username)
    else:
        form = TreeForm()

    if get_user_agent(request).is_mobile | get_user_agent(request).is_tablet:
        
        return render_to_response("tree_form_mob.html", {'form': form},
            context_instance=RequestContext(request))
    else:  
            
        return render_to_response("tree_form.html", {'form': form},
            context_instance=RequestContext(request))

@login_required
def tree_update(request, nr_tree):
    tree = get_object_or_404(Tree, usuario=request.user, id=nr_tree)
    if request.method == "POST":
        form = TreeForm(request.POST, request.FILES, instance=tree)
        if form.is_valid():
            form.save()
            return redirect('user_tree_list', username=request.user.username)
    else:
        form = TreeForm(instance=tree)
    
    if get_user_agent(request).is_mobile | get_user_agent(request).is_tablet:
        
        return render_to_response("tree_form_mob.html", {'form': form},
            context_instance=RequestContext(request))
    else:  
            
        return render_to_response("tree_form.html", {'form': form},
            context_instance=RequestContext(request))

@login_required
def tree_delete(request, nr_tree):
    tree = get_object_or_404(Tree, usuario=request.user, id=nr_tree)
    if request.method == "POST":
        
        tree.delete()
        return redirect('user_tree_list', username=request.user.username)

    if get_user_agent(request).is_mobile | get_user_agent(request).is_tablet:
        return render_to_response("confirm_delete_tree_mob.html", {'object': tree},
                context_instance=RequestContext(request))
    else:
        return render_to_response("confirm_delete_tree.html", {'object': tree},
                context_instance=RequestContext(request))

#Lista com Busca de Árvores
class SearchTreeList(ListView):
    form_class = None
 
    def get_context_data(self, **kwargs):
        context = super(SearchTreeList, self).get_context_data(**kwargs)
        context['frm_srch'] = self.get_form()
        qs_data = context['frm_srch'].data
        context['query_string'] = ''
        if qs_data:
            qs_data.pop('page', '1')
            context['query_string'] = qs_data.urlencode()
        return context
 
    def get_queryset(self):
        if self.form_class is None:
            return super(SearchTreeList, self).get_queryset()
        return self.get_form().get_queryset()
 
    def get_form(self):
        return self.form_class(self.request.GET.copy() or None)

class TreeList(SearchTreeList):
    form_class = SearchTreeForm
    paginate_by = 20
    
    def get_template_names(self):
        if get_user_agent(self.request).is_mobile | get_user_agent(self.request).is_tablet:
            return "core/tree_list_mob.html"
        else:  
            return 'core/tree_list.html'
    
tree_list = TreeList.as_view()

#Lista de Árvores do Usuário
class TreeListView(ListView):
    model = Tree
    
    def get_template_names(self):
        if get_user_agent(self.request).is_mobile | get_user_agent(self.request).is_tablet:
            return "core/user_tree_list_mob.html"
        else:  
            return 'core/user_tree_list.html'

    def get_context_data(self, **kwargs):
        context = super(TreeListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return super(TreeListView, self).get_queryset().filter(usuario=self.request.user)

user_tree_list = TreeListView.as_view()

class TreeDetailView(DetailView):

    def get_template_names(self):
        if get_user_agent(self.request).is_mobile | get_user_agent(self.request).is_tablet:
            return "tree_detail_mob.html"
        else:  
            return 'tree_detail.html'
    queryset = Tree.objects

tree_detail = TreeDetailView.as_view()

# Views para aplicativo Android
@api_view(['GET', 'POST'])
def tree_list_android(request, format=None):
    parser_classes = (MultiPartParser, FormParser, FileUploadParser,)
    permission_classes = (AllowAny)
    
    if request.method == 'GET':
        trees = Tree.objects.all()
        serializer = TreeSerializer(trees, many=True)
        return Response(serializer.data, content_type='application/json; charset=utf-8')

    elif request.method == 'POST':
       
        serializer = TreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class UserDetailsView(RetrieveUpdateAPIView):

    """
    Returns User's details in JSON format.
    Accepts the following GET parameters: token
    Accepts the following POST parameters:
        Required: token
        Optional: email, first_name, last_name and UserProfile fields
    Returns the updated UserProfile and/or User object.
    """
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user

class LoginView(GenericAPIView):

    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework
    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    token_model = Token
    response_serializer = UserDetailsSerializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.token, created = self.token_model.objects.get_or_create(
            user=self.user)
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            login(self.request, self.user)

    def get_response(self):
        return Response(
            self.response_serializer(self.user).data, 
                status=status.HTTP_200_OK
        )

    def get_error_response(self):
        return Response(
            self.serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=self.request.data)
        if not self.serializer.is_valid():
            return self.get_error_response()
        self.login()
        return self.get_response()