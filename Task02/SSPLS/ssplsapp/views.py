from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.loader import get_template
from django.template import Context
from .forms import ContactForm
from .models import Game, User
def index(request):
	context_data = ""
	return render(request, 'index.html', dict(context_data))
def playedgames(request):
	context_data = ""
	return render(request, 'played-games.html', dict(context_data))
def availablegames(request):
	context_data = ""
	return render(request, 'available-games.html', dict(context_data))
def statistics(request):
	context_data = ""
	return render(request, 'statistics.html', dict(context_data))
def playgame(request):
	context_data = ""
	return render(request, 'play-game.html', dict(context_data))
def creategame(request):
	context_data = ""
	return render(request, 'create-game.html', dict(context_data))
def game(request):
	context_data = ""
	return render(request, 'game-result.html', dict(context_data))
def addgame(reguest):
    context_data = ""
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            bet = form.cleaned_data['bet']
            #вставка в базу
            u1 = User.objects.get(username='test1')
            u2 = User.objects.get(username='np')
            g = Game(firstuser=u1,seconduser=u2,firstbet=bet,secondbet='nb',status='np')
            g.save()
            return HttpResponse(bet)
        else:
            return HttpResponse('invalid')
    else:
        form = ContactForm()
    #Выводим форму в шаблон
    return HttpResponse('nopost')