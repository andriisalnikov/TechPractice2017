from django.contrib import admin
from .models import MyObject, MyFile

admin.site.register(MyObject)
admin.site.register(MyFile)