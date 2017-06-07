# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Friend, Profile, Friend_request
# Register your models here.
admin.site.register(Friend)
admin.site.register(Profile)
admin.site.register(Friend_request)