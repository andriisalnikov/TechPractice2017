from django.db import models

from polls.models.User import User


class Competition(models.Model):
    id = models.IntegerField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="")
