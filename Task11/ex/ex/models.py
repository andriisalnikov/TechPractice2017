from django.db import models
from django.utils import timezone

# Create your models here.


def seven_days_hence():
    return timezone.now() + timezone.timedelta(days=7)


class TheUser(models.Model):
    nick = models.CharField(max_length=4096)
    password_hash = models.CharField(max_length=128)
    email = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now)
    validation = models.BooleanField(default=False)

    def __str__(self):
        return self.nick


class FileSet(models.Model):
    name = models.CharField(max_length=4096)
    user = models.ForeignKey(TheUser)
    password_hash = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=4096, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    changed_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(default=seven_days_hence)

    def __str__(self):
        return self.name


class TheFile(models.Model):
    fileset = models.ForeignKey(FileSet)
    name = models.CharField(max_length=4096)
    qty = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
