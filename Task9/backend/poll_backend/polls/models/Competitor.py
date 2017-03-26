from django.db import models
from polls.models.Competition import Competition


class Competitor(models.Model):
    class Meta:
        managed = True
    id = models.IntegerField(primary_key=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200, default="")
    lastName = models.CharField(max_length=200, default="")
    course = models.IntegerField(min_value=1, max_value=6, default=1)
    speciality = models.CharField(max_length=100, default="")
