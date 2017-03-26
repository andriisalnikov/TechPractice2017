from django.db import models
from polls.models import Competitor, Category

from polls.models import User


class Vote(models.Model):
    class Meta:
        managed = True,
        unique_together = ("category", "voter")
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
