from django.db import models


class Competition(models.Model):
    id = models.IntegerField()
    name = models.CharField()
