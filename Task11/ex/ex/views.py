from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import TheUser, FileSet, TheFile, Codes
import datetime
import hashlib
import random
import string

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)


def index(request):
    objects_list = FileSet.objects.order_by('key')
    template = loader.get_template('index.html')
    context = { 'objects_list': objects_list }
    return HttpResponse(template.render(context, request))


def object_view(request, obj_id):
    my_object = FileSet.objects.filter(pk=obj_id)
    files_list = TheFile.objects.filter(object_id=obj_id)
    template = loader.get_template('../Frontend_HERE/object_view.html')
    context = {
        'my_object': my_object[0],
        'files_list': files_list
    }
    return HttpResponse(template.render(context, request))


def testform(request):
    array = { 1:'one', 2:'two', 3:'three' }
    template = loader.get_template('../Frontend_HERE/testform.html')
    context = {
        'error_message': 'no errors still',
        'headertext': 'Test Form',
        'array': array
    }
    return HttpResponse(template.render(context, request))


def registration(request):
    if request.method == 'POST':
        template = loader.get_template('../Frontend_HERE/../templates/message.html')
        nick_is_used = len(TheUser.objects.filter(nick=request.POST['nick'])) > 0
        mail_is_used = len(TheUser.objects.filter(email=request.POST['email'])) > 0
        messages = []
        if nick_is_used:
            messages.append('Sorry, Nick ' + request.POST['nick'] + ' is already in use.')
        if mail_is_used:
            messages.append('Sorry, E-mail ' + request.POST['email'] + ' is already in use.')
        context = { 'messages': messages }
        if (not nick_is_used) & (not mail_is_used):
            password = request.POST['password']
            salt = "vex"
            m = hashlib.md5()
            m.update(salt.encode('utf-8') + password.encode('utf-8'))
            u = TheUser(nick=request.POST['nick'], password_hash=m.hexdigest(), email=request.POST['email'])
            u.save()
            somecode = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))
            p = Codes(user=u, code=somecode)
            p.save()
            context = {'messages': ['Thanks for registration! Confirmation link was sent to email ' + request.POST['email']]}
        return HttpResponse(template.render(context, request))

    else:
        template = loader.get_template('registration.html')
        context = {}
        return HttpResponse(template.render(context, request))

