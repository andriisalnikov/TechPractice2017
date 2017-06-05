from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from .models import TheUser, FileSet, TheFile, Codes
from django.core.mail import send_mail
import hashlib
import random
import string


def passwordHash(password):
    m = hashlib.md5()
    salt = "vex"
    m.update(salt.encode('utf-8') + password.encode('utf-8'))
    return m.hexdigest()

def randomStringUpperAndDigits(length):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))

def randomStringJustDigits(length):
    return ''.join(random.SystemRandom().choice(string.digits) for _ in range(length))

def index(request):
    message = ''
    if request.method == 'POST':
        users = TheUser.objects.filter(nick=request.POST['nick'], password_hash=passwordHash(request.POST['password']))
        if len(users) == 1:
            if users[0].validation:
                request.session['nick'] = request.POST['nick']
                return redirect('myprofile')
            else:
                message = 'Please validate your account! Validation link was sent to your email.'
        else:
            message = 'Logic/password is incorrect'
    template = loader.get_template('index.html')
    nick = 'guest'
    try:
        nick = request.session['nick']
    except KeyError:
        pass
    context = {'message': message, 'nick': nick}
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
        if (not nick_is_used) & (not mail_is_used):
            somecode = randomStringUpperAndDigits(32)
            mail_was_sent = send_mail(
                'VEX.NET validation',
                'Here is your validation link: http://127.0.0.1:8000/validation/?nick=' + request.POST[
                    'nick'] + '&code=' + somecode,
                'vex.validation@gmail.com',
                [request.POST['email']],
                fail_silently=False,
            )
            if mail_was_sent:
                u = TheUser(nick=request.POST['nick'], password_hash=passwordHash(request.POST['password']), email=request.POST['email'])
                u.save()
                p = Codes(user=u, code=somecode)
                p.save()
                messages.append('Thanks for registration! Confirmation link was sent to email ' + request.POST['email'])
            else:
                messages.append('Email was not sent! Please try again later.')
        context = {'messages': messages}
        return HttpResponse(template.render(context, request))

    else:
        template = loader.get_template('registration.html')
        context = {}
        return HttpResponse(template.render(context, request))


def validation(request):
    messages = ['Sorry! Something went wrong(((']
    if request.method == 'GET':
        u = TheUser.objects.filter(nick=request.GET['nick'])
        c = Codes.objects.filter(code=request.GET['code'], user=u[0])
        if (len(u) > 0) & (len(c) == 1):
            u.update(validation=True)
            messages = ['Congratulations! Your account was successfully validated']
            c.delete()
    template = loader.get_template('message.html')
    context = {'messages': messages}
    return HttpResponse(template.render(context, request))


def myprofile(request):
    u = TheUser.objects.filter(nick=request.session['nick'])
    filesets = FileSet.objects.filter(user=u)
    template = loader.get_template('myprofile.html')
    context = {'nick': request.session['nick'], 'filesets': filesets}
    return HttpResponse(template.render(context, request))


def create_fileset(request):
    au = TheUser.objects.filter(nick=request.session['nick'])
    somekey = randomStringJustDigits(12)
    fileset = FileSet(name=somekey, user=au[0])
    fileset.save()
    return redirect('/' + fileset.name.__str__() + '/')


def fileset(request, fileset_name):
    f = FileSet.objects.get(name=fileset_name)
    template = loader.get_template('fileset.html')
    try:
        if f.user.nick == request.session['nick']:
            template = loader.get_template('fileset_for_owner.html')
    except KeyError:
        pass
    files = TheFile.objects.filter(fileset=f)
    context = {'fileset': f, 'files': files}
    return HttpResponse(template.render(context, request))


def change_description(request, fileset_name):
    if request.method == 'POST':
        f = FileSet.objects.filter(name=fileset_name)
        f.update(description=request.POST['description'])
    return redirect('/' + fileset_name.__str__() + '/')


def logout(request):
    try:
        request.session.flush()
    except KeyError:
        pass
    return redirect('index')


def upload_file(request, fileset_name):
    if request.method == 'POST':
        f = FileSet.objects.filter(name=fileset_name)
        handle_uploaded_file(request.FILES['somefile'])
        thatfile = TheFile(fileset=f[0], name=request.FILES['somefile'].name)
        thatfile.save()
    return redirect('/' + fileset_name + '/')


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
