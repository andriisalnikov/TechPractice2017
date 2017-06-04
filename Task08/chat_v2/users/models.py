# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    block_expire = models.DateTimeField(default=datetime.datetime.now, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos', default='profile_photos/profile_image_default.png')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Friend(models.Model):
    users = models.ManyToManyField(User, blank=True)
    current_user = models.ForeignKey(User, related_name='owner')

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )   
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )   
        friend.users.remove(new_friend)

class Friend_request(models.Model):

    requests_sent = models.ManyToManyField(User, related_name="requests_sent", blank=True)
    requests_received = models.ManyToManyField(User, related_name="requests_received", blank=True)
    current_user = models.ForeignKey(User, related_name='requests_owner')
