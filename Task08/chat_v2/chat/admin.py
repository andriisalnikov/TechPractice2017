# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import ChatMessage, Chat_room, Chat_group, GroupChatMessage, MessageReport

# Register your models here.

admin.site.register(ChatMessage)
admin.site.register(Chat_room)
admin.site.register(Chat_group)
admin.site.register(GroupChatMessage)
admin.site.register(MessageReport)
