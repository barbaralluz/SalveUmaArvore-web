# coding: utf-8

from django.conf.urls import patterns, url, include
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'tg.core.views.index', name="index"),
    url(r'^control_panel/$', 'tg.core.views.control_panel', name="control_panel"),
    url(r'^profile/$', 'tg.core.views.profile', name="profile"),

    #Mapa
    url(r'^map/$', 'tg.core.views.map', name="map"),

    url(r'^create/map/$', 'tg.core.views.map_create', name="map_form"),
    url(r'^update/map/(?P<nr_map>\d+)/$', 'tg.core.views.map_update', name="map_form"),

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
    
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', 
                    {'template_name': 'change_password.html'}, name='password_change'),
    
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', 
                    {'template_name': 'change_password_done.html'}, name='password_change_done'),

    url(r'', include('social_auth.urls')),

    # Admin	
    url(r'^admin/', include(admin.site.urls)),

    
)




if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))