"""
Definition of models.
"""

from django.db import models

# Create your models here.

class USER(models.Model):
    id = models.AutoField("ID", primary_key=True)
    name = models.CharField("name", max_length=20)
    login = models.CharField("nickname", max_length=20)
    email = models.CharField("e-mail", max_length=50)
    password = models.CharField("password", max_length=30)
    city = models.CharField("city", max_length=30)
    pass

class EVENT(models.Model):
    id = models.AutoField("ID", primary_key=True)
    name = models.CharField("event name", max_length=50)
    details = models.TextField()
    place = models.CharField("where", max_length=40)
    date = models.DateField("when")
    participants = models.ManyToManyField(USER)
    votingStart = models.DateField()
    votingEnd = models.DateField()
    pass

class MDATE(models.Model):
    id = models.AutoField(primary_key=True)
    meetingDateTimeS = models.DateField()
    
class EVTDATE(models.Model):
    id = models.AutField(primary_key=True)
    evt = models.ForeignKey(EVENT)
    dat = models.ForeignKey(MDATE)
    
class VOTE(models.Model):
    id = models.AutoField(primary_key=True)
    edate = models.ForeignKey(EVTDATE)
    usr = models.ForeignKey(USER)

def CreateUser(n, l, e, pas, c):
    from practice.db.models import USER
    usr = USER(name=n, login=l, email=e, password=pas, city=c)
    usr.save()

def CreateEvent(nam, det, pla, vst, ven)
    from practice.db.models import EVENT
    evt = EVENT(name=nam, details=det, place=pla, votingStart=vst, votingEnd=ven)
    evt.save()
    
def Participate(user, event):
    from practice.db.models import USER
    from practice.db.models import EVENT
    event.participants.add(user)
    event.save()
    
def DisplayAll(event):
    from practice.db.models import EVENT
    for e in EVENT.objects.all():
        print(e.name)
        
def DisMostPop(event):
    from practice.db.models import EVENT
    from practice.db.models import Max
    from practice.db.models import Count
    EVENT.objects.all().aggregate(Max(EVENT.objects.count('participants'))) /*?*/
    
    

