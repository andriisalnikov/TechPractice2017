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
    """Renders the order_asc page."""
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
    """Renders the order_desc page."""
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


def rnd_evnt(request):
    """Renders the random event page."""
    assert isinstance(request, HttpRequest)

    all_event = models.GetAllEvent() 
    
    from random import randint
    ent_indx = randint(0,len(all_event) - 1)
    rnd_event = all_event[ent_indx]

    return render(
        request,
        'app/event.html',
        {
            'title':'Випадкова подія',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'event':rnd_event
        }
    ) 


def creating(request):
    
    return render(
        request,
        'app/creating.html',
        {
            'title':'створення нової події'
        }
    ) 

def stats(request):

    all_evnt_count = models.GetAllEventsCount()
    vouted_user_count = models.GetVotedUsersCount()

    return render(
        request,
        'app/stats.html',
        {
            'title':'Статисика створенних подій',
            'all_evnt_count':all_evnt_count,
            'vouted_user_count':vouted_user_count
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

from app.forms import NewEventForm
def creating(request):

    evt_title = "no title"
    evt_description = "no description"
    evt_date = datetime.now()
    evt_vote_start = datetime.now()
    evt_vote_end = datetime.now()

    if request.method == "POST":
        # Get the posted form
        eventForm = NewEventForm(request.POST)

        if eventForm.is_valid():
            evt_title = eventForm.cleaned_data['evt_title']
            evt_description = eventForm.cleaned_data['evt_description']
            evt_date = eventForm.cleaned_data['evt_date']
            evt_vote_start = eventForm.cleaned_data['evt_vote_start']
            evt_vote_end = eventForm.cleaned_data['evt_vote_end']
    else:
        eventForm = NewEventForm()

    return render(
        request,
        'app/creating.html',
        {
            'title': 'створення нової події',
            'evt_title': evt_title,
            'evt_description': evt_description,
            'evt_date': evt_date,
            'evt_vote_start': evt_vote_start,
            'evt_vote_end': evt_vote_end
        }
    )
