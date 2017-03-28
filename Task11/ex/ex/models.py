from django.db import models
from django.utils import timezone

# Create your models here.


# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title
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

class MyFile(models.Model):
    object_id = models.ForeignKey(MyObject)
    file = models.FileField()