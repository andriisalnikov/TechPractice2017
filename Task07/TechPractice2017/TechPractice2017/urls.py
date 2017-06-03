# -*- coding: utf-8 -*-
"""
Definition of urls for TechPractice2017.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^about', app.views.about, name='about'),
    url(r'^order_asc', app.views.order_asc, name='order_asc'),
    url(r'^order_desc', app.views.order_desc, name='order_desc'),
    url(r'^rnd_evnt', app.views.rnd_evnt, name='rnd_evnt'),
    url(r'^creating', app.views.creating, name='creating'),
    url(r'^stats', app.views.stats,name='stats'),

    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
