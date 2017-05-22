from django.contrib import admin
from .models import TheUser, FileSet, TheFile

admin.site.register(TheUser)
admin.site.register(FileSet)
admin.site.register(TheFile)
