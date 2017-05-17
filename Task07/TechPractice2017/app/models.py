"""
Definition of models.
"""

from django.db import models

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
    evtdateid = models.AutField(primary_key=True)
    evt = models.ForeignKey(EVENT)
    dat = models.ForeignKey(MDATE)
    
class VOTE(models.Model):
    voteid = models.AutoField(primary_key=True)
    edate = models.ForeignKey(EVTDATE)
    usr = models.ForeignKey(USER)
    
###############################################################################################################################

def CreateUser(n, l, e, pas, c):
    from practice.db.models import USER
    usr = USER(name=n, login=l, email=e, password=pas, city=c)
    usr.save()

def GetUserInfo(uid):
    from practice.db.models import USER
    person = USER.objects.get(userid=uid)
    pass

def EditUserName(uid, uname):
    from practice.db.models import USER
    USER.objects.filter(userid=uid).update(name=uname)
    
def EditEmail(uid, mail):
    from practice.db.models import USER
    USER.objects.filter(userid=uid).update(email=mail)
    
def EditCity(uid, c):
    from practice.db.models import USER
    USER.objects.filter(userid=uid).update(city=c)

################################################################################################################################

def CreateEvent(nam): #event creation method
    from practice.db.models import EVENT
    evt = EVENT(name=nam)
    evt.save()
    
def EditEvtDetails(detls, evid): #editing event details (can be NULL first)
    from practice.db.models import EVENT
    EVENT.objects.filter(id=evid).update(details=detls)

def EditEvtPlace(pla, evid): #editing event place (can be NULL first)
    from practice.db.models import EVENT
    EVENT.objects.filter(id=evid).update(place=pla)
    
def EditEvtVotingPeriod(vst, ven, evid): #editing event voting period (can be NULL first, requires both start and end dates)
    from practice.db.models import EVENT
    EVENT.objects.filter(id=evid).update(votingStart=vst, votingEnd=ven)
    
def GetEventInfo(evtid): #returns event object on necessary id
    from practice.db.models import EVENT
    evt = EVENT.objects.get(id=evtid)
    return evt
    
def DisplayAll(event): #returns all events (not finished!)
    from practice.db.models import EVENT
    allevents=[]
    for e in EVENT.objects.all():
         allevents.add(e)
    return allevents
        
def DisMostPop(event):
    from practice.db.models import EVENT
    from practice.db.models import Max
    from practice.db.models import Count
    EVENT.objects.order_by(EVENT.objects.annotate(partcount=Count('participants'))).aggregate(Max(partcount))
    pass #finish!!!
    
def Participate(user, event):
    from practice.db.models import USER
    from practice.db.models import EVENT
    event.participants.add(user)
    event.save()
