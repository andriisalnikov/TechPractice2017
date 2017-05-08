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
    pass

  
