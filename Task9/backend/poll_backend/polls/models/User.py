from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    vkId = models.CharField(default="")
    facebookId = models.CharField(default="")
    googleId = models.CharField(default="")
