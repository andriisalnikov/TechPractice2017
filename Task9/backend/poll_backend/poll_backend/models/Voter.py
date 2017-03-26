from django.db import models


class Voter(models.Model):
    id: models.IntegerField()
    vkId: models.CharField()
    facebookId: models.CharField()
    googleId: models.CharField()
