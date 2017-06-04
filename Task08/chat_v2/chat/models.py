# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Chat_room(models.Model):

    background_color = models.CharField(max_length=10, default="ffffff")
    title = models.CharField(max_length=30, default="chat-room")
    user1 = models.ForeignKey(User, null=True, related_name="user1")
    user2 = models.ForeignKey(User, null=True, related_name="user2")

class Chat_group(models.Model):

    users = models.ManyToManyField(User)
    background_color = models.CharField(max_length=10, default="ffffff")
    title = models.CharField(max_length=30, default="chat-room")
    global_group = models.BooleanField(default=False)
    chat_admin = models.ForeignKey(User, null=True, related_name="chat_admin")

    def __str__(self):
        return self.title

class ChatMessage(models.Model):

    message = models.CharField(max_length=255)
    room = models.ForeignKey(Chat_room, null=True)
    user = models.ForeignKey(User, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    username = models.CharField(max_length=255, null=True)
    user_image = models.CharField(max_length=255, null=True)
    content_type = models.CharField(max_length=10, null=True)

class GroupChatMessage(models.Model):

    message = models.CharField(max_length=255)
    group = models.ForeignKey(Chat_group, null=True)
    user = models.ForeignKey(User, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    username = models.CharField(max_length=255, null=True)
    user_image = models.CharField(max_length=255, null=True)
    content_type = models.CharField(max_length=10, null=True)

class MessageReport(models.Model):
    reported_by = models.ForeignKey(User, related_name="reported_by", null=True)
    reported_user = models.ForeignKey(User, related_name="reported_user")
    message = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True)
    content_type = models.CharField(max_length=10, null=True)