from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import MyFile
from .models import MyObject
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)

def index(request):
    objects_list = MyObject.objects.order_by('key')
    template = loader.get_template('index.html')
    context = { 'objects_list': objects_list }
    return HttpResponse(template.render(context, request))

def object_view(request, obj_id):
    my_object = MyObject.objects.filter(pk=obj_id)
    files_list = MyFile.objects.filter(object_id=obj_id)
    template = loader.get_template('object_view.html')
    context = {
        'my_object': my_object[0],
        'files_list': files_list
    }
    return HttpResponse(template.render(context, request))