from django.db import models
from django.utils import timezone

# Create your models here.

def seven_days_hence():
    return timezone.now() + timezone.timedelta(days=7)

class MyObject(models.Model):
    key = models.CharField(max_length=32)
    description = models.CharField(max_length=4096, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    changed_date = models.DateTimeField(default=timezone.now)
    deletion_date = models.DateTimeField(default=seven_days_hence)

    def __str__(self):
        return str(self.key)

class MyFile(models.Model):
    object_id = models.ForeignKey(MyObject)
    file = models.FileField()

    def __str__(self):
        return self.file.name