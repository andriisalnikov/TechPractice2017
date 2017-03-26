from django.db import models
from .Competition import Competition


class Competitor(models.Model):
    id = models.IntegerField()
    competition = models.ForeignKey(Competition)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    course = models.IntegerField(min_value=1, max_value=6)
    speciality = models.CharField(max_length=100)
