from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'tg.arvore.views.index', name="index"),
 
    # Arvores
    url(r'^list/tree/$', 'tg.arvore.views.arvore_list', name="arvore_list"),
    url(r'^create/tree/$', 'tg.arvore.views.arvore_create', name="arvore_form"),
    url(r'^update/tree/(?P<nr_arvore>\d+)/$', 'tg.arvore.views.arvore_update', name="arvore_form"),
    url(r'^delete/tree/(?P<nr_arvore>\d+)/$', 'tg.arvore.views.arvore_delete', name="arvore_delete"),
	
    # Autenticacao e Login
    url(r'^registrar/$', 'tg.arvore.views.registrar', name="registrar"),

    url(r'^login/$', 'django.contrib.auth.views.login',
                    {'template_name': 'login.html' }),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
                    {'login_url': '/login/'}),

    # Admin	
    url(r'^admin/', include(admin.site.urls)),
)


