from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import TheUser, FileSet, TheFile, Codes
from django.core.mail import send_mail
import hashlib
import random
import string


def index(request):
    objects_list = FileSet.objects.order_by('key')
    template = loader.get_template('index.html')
    context = { 'objects_list': objects_list }
    return HttpResponse(template.render(context, request))


def registration(request):
    if request.method == 'POST':
        template = loader.get_template('message.html')
        nick_is_used = len(TheUser.objects.filter(nick=request.POST['nick'])) > 0
        mail_is_used = len(TheUser.objects.filter(email=request.POST['email'])) > 0
        messages = []
        if nick_is_used:
            messages.append('Sorry, Nick ' + request.POST['nick'] + ' is already in use.')
        if mail_is_used:
            messages.append('Sorry, E-mail ' + request.POST['email'] + ' is already in use.')
        context = {'messages': messages}
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
            send_mail(
                'VEX.NET validation',
                'Here is your validation link: http://127.0.0.1:8000/validation/?nick=' + request.POST['nick'] + '&code=' + somecode,
                'vex.validation@gmail.com',
                [request.POST['email']],
                fail_silently=False,
            )
            context = {'messages': ['Thanks for registration! Confirmation link was sent to email ' + request.POST['email']]}
        return HttpResponse(template.render(context, request))

    else:
        template = loader.get_template('registration.html')
        context = {}
        return HttpResponse(template.render(context, request))


def validation(request):
    messages = ['Sorry! Something went wrong(((']
    if request.method == 'GET':
        u = TheUser.objects.filter(nick=request.GET['nick'])
        if len(u) > 0 & len(Codes.objects.filter(code=request.GET['code'], user=u[0])) == 1:
            u.update(validation=True)
            messages = ['Congratulations! Your account was successfully validated']
    template = loader.get_template('message.html')
    context = {'messages': messages}
    return HttpResponse(template.render(context, request))

