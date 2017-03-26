from django.db import models
from poll_backend.models import Competitor, Category, Voter


class Vote(models.Model):
    competitor = models.ForeignKey(Competitor)
    category = models.ForeignKey(Category)
    voter = models.ForeignKey(Voter)
