# -*- coding: utf-8 -*-
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app import models

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    all_event = models.GetAllEvent() 

    return render(
        request,
        'app/index.html',
        {
            'title':'Домашня сторінка',
            'year':datetime.now().year,
            'all_event':all_event
        }
    )

def order_asc(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    all_event = models.DisMostPop()

    return render(
        request,
        'app/index.html',
        {
            'title':'Найбільш популярні',
            'year':datetime.now().year,
            'all_event':all_event
        }
    )

def order_desc(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    all_event = models.DisLessPop()

    return render(
        request,
        'app/index.html',
        {
            'title':'Найменш популярні',
            'year':datetime.now().year,
            'all_event':all_event
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О чому?',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
