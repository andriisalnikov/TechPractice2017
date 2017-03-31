from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    vkId = models.CharField(null=True, max_length=300)
    facebookId = models.CharField(null=True, max_length=300)
    googleId = models.CharField(null=True, max_length=300)


class Competition(models.Model):
    id = models.IntegerField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=200)

    def as_json(self):
        return dict(id=self.id, creatorId=self.creator.id, name=self.name)


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

    def as_json(self):
        return dict(id=self.id, creatorId=self.competition.id, name=self.name)


class Competitor(models.Model):
    id = models.IntegerField(primary_key=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200, default="")
    lastName = models.CharField(max_length=200, default="")
    course = models.IntegerField(default=1)
    speciality = models.CharField(max_length=100, default="")


class Vote(models.Model):
    class Meta:
        managed = True,
        unique_together = ("category", "voter")
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
