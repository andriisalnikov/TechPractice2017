from django.db import models
from .Competition import Competition


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
