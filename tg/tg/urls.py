# coding: utf-8

from django.conf.urls import patterns, url, include
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from tg.core.views import FacebookLogin, UserDetailsView, LoginView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'tg.core.views.index', name="index"),
    url(r'^statistics/$', 'tg.core.views.statistics', name="statistics"),

    #Municipios
    url(r'^municipios_app/', include('municipios.urls')),

    # Árvores
    
    #Lista com Todas as Árvores
    url(r'^list/tree/$', 'tg.core.views.tree_list', name="tree_list"),

    #Lista com Árvores do Usuário
    url(r'^(?P<username>\w+)/list/tree/$', 'tg.core.views.user_tree_list', name="user_tree_list"),
    url(r'^create/tree/$', 'tg.core.views.tree_create', name="tree_form"),
    url(r'^update/tree/(?P<nr_tree>\d+)/$', 'tg.core.views.tree_update', name="tree_form"),
    url(r'^detail/tree/(?P<pk>\d+)/$', 'tg.core.views.tree_detail', name="tree_detail"),
    url(r'^delete/tree/(?P<nr_tree>\d+)/$', 'tg.core.views.tree_delete', name="tree_delete"),
	
    # Autenticação e Login
    url(r'^signin/$', 'tg.core.views.signin', name='signin'),

    url(r'^login/$', 'tg.core.views.log_in', name='login'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
                    {'login_url': '/'}),

    url(r'', include('social_auth.urls')),

    # Admin	
    url(r'^admin/', include(admin.site.urls)),

    # Coments
    url(r'^comments/', include('fluent_comments.urls')),

    #Rest Android
    #Árvores
    url(r'^trees/$', 'tg.core.views.tree_list_android'),
    #Autenticação
    url(r'^rest-auth/', include('rest_auth.urls')),
    (r'^rest-auth/', include('rest_auth.urls')),
    (r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/user/logged/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^rest-auth/loggin/$', LoginView.as_view(), name='rest_login'),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))