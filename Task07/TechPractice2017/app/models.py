# -*- coding: utf-8 -*-
"""
Definition of models.
"""

from django.db import models
import numpy as np

# Create your models here.

class USER(models.Model):
    userid = models.AutoField("ID", primary_key=True)
    name = models.CharField("name", max_length=20)
    login = models.CharField("nickname", max_length=20)
    email = models.CharField("e-mail", max_length=50)
    password = models.CharField("password", max_length=30)
    city = models.CharField("city", max_length=30, blank=True)
    pass

class EVENT(models.Model):
    eventid = models.AutoField("ID", primary_key=True)
    name = models.CharField("event name", max_length=50)
    details = models.TextField("details", blank=True)
    place = models.CharField("where", max_length=40, blank=True)
    date = models.DateField("when", blank=True)
    participants = models.ManyToManyField(USER, blank=True)
    votingStart = models.DateField(blank=True)
    votingEnd = models.DateField(blank=True)

    pass

class MDATE(models.Model):
    mdateid = models.AutoField(primary_key=True)
    meetingDateTimeS = models.DateField()
    
class EVTDATE(models.Model):
    evtdateid = models.AutoField(primary_key=True)
    evt = models.ForeignKey(EVENT)
    dat = models.ForeignKey(MDATE)
    
class VOTE(models.Model):
    voteid = models.AutoField(primary_key=True)
    edate = models.ForeignKey(EVTDATE)
    usr = models.ForeignKey(USER)
    
###############################################################################################################################
def MakeVote(evtdate, participant):
    '''participant must be typeof USER!!!'''
    from app.models import USER
    from app.models import EVTDATE
    from app.models import VOTE
    partevent=evtdate.get(evt)
    Participate(participant, partevnt)
    vt=VOTE(edate=evtdt, usr=participant)
    vt.save()
    
def MakePossibleDate(dt):
    from app.model import MDATE
    dt=MDATE(meetingDateTimeS=date)
    dt.save()

def MakePairDateEvent(mdate, evnt):
    from app.model import MDATE
    from app.model import EVTDATE
    evtdt=EVTDATE(evt=evnt, dat=mdate)
    evtdt.save()
###############################################################################################################################


def CreateUser(n, l, e, pas, c):
    from app.models import USER
    usr = USER(name=n, login=l, email=e, password=pas, city=c)
    usr.save()

def GetUserInfo(uid):
    from app.models import USER
    person = USER.objects.get(userid=uid)
    pass

def EditUserName(uid, uname):
    from app.models import USER
    USER.objects.filter(userid=uid).update(name=uname)
    
def EditEmail(uid, mail):
    from app.models import USER
    USER.objects.filter(userid=uid).update(email=mail)
    
def EditCity(uid, c):
    from app.models import USER
    USER.objects.filter(userid=uid).update(city=c)

################################################################################################################################

def CreateEvent(nam): #event creation method
    from app.models import EVENT
    evt = EVENT(name=nam)
    evt.save()


def CreateEventTotal(name,descript,init_date,vote_start_date,vote_end_date) :
    from app.models import EVENT
    evt = EVENT(name=name,details=descript,place='РФФ',date=init_date,votingStart=vote_start_date,votingEnd=vote_end_date)
    evt.save()


    
def EditEvtDetails(detls, evid): #editing event details (can be NULL first)
    from app.models import EVENT
    EVENT.objects.filter(id=evid).update(details=detls)

def EditEvtPlace(pla, evid): #editing event place (can be NULL first)
    from app.models import EVENT
    EVENT.objects.filter(id=evid).update(place=pla)
    
def EditEvtVotingPeriod(vst, ven, evid): #editing event voting period (can be NULL first, requires both start and end dates)
    from app.models import EVENT
    EVENT.objects.filter(id=evid).update(votingStart=vst, votingEnd=ven)
    
def GetEventInfo(evtid):
    '''returns event object on necessary id'''
    from app.models import EVENT
    evt = EVENT.objects.get(id=evtid)
    return evt
    

def GetAllEvent():
    '''return all event'''
    from app.models import EVENT 
    evt = EVENT.objects.all()
    return evt

def GetAllEventOrder(order, reverse):
    '''return all event'''
    from app.models import EVENT
    evt = EVENT.objects.order_by(-order)
    return evt

def DisplayAll(event): #returns all events (not finished!)
    from app.models import EVENT
    allevents=[]
    for e in EVENT.objects.all():
         allevents.add(e)
    return allevents
        

def DisLessPop():
    from app.models import EVENT
    
    all_evnt = EVENT.objects.all()
    part_count = []
    for t in all_evnt.annotate(evnt_count=models.Count('participants')):
        part_count.append(t.evnt_count)

    order = np.argsort(part_count)
    all_evnt = np.array(all_evnt)
    all_evnt = all_evnt[ order ]

    return all_evnt 
    pass #finish!!!

def DisMostPop():
    from app.models import EVENT

    all_evnt = EVENT.objects.all()
    part_count = []
    for t in all_evnt.annotate(evnt_count=models.Count('participants')):
        part_count.append(t.evnt_count)

    order = np.argsort(part_count)[::-1]
    all_evnt = np.array(all_evnt)

    all_evnt_list = []
    for o in order :
        curr_evnt = all_evnt[o]
        all_evnt_list.append(curr_evnt)

    return all_evnt_list
    pass  # finish!!!


def Participate(user, event):
    from app.models import USER
    from app.models import EVENT
    event.participants.add(user)
    event.save()

def GetParticipantsCount(event):
    from app.models import EVENT
    partList=event.participants.all()
    return len(partList)

def Get

-#Statistics ------------------------------------------------------################################
 -def GetAllEventsCount():
 -    from app.models import EVENT
 -    eList = (EVENT.objects.values('eventid').distinct())
 -    return len(eList)
 -
 -def GetVotedUsersCount():
 -    from app.models import VOTE
 -    from django.db.models import Count
 -    uList = (VOTE.objects.values('usr').distinct())
 -    return len(uList) 

