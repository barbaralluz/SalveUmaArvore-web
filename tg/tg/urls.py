# coding: utf-8

from django.conf.urls import patterns, url, include
from django.views.generic.base import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'tg.core.views.index', name="index"),
    url(r'^profile/$', 'tg.core.views.profile', name="profile"),
 
    # Árvores
    url(r'^list/tree/$', 'tg.core.views.tree_list', name="tree_list"),
    url(r'^create/tree/$', 'tg.core.views.tree_create', name="tree_form"),
    url(r'^update/tree/(?P<nr_tree>\d+)/$', 'tg.core.views.tree_update', name="tree_form"),
    url(r'^delete/tree/(?P<nr_tree>\d+)/$', 'tg.core.views.tree_delete', name="tree_delete"),
	
    # Autenticação e Login
    url(r'^signin/$', 'tg.core.views.signin', name='signin'),

    url(r'^login/$', 'tg.core.views.log_in', name='login'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
                    {'login_url': 'login'}),

    # Admin	
    url(r'^admin/', include(admin.site.urls)),


)


