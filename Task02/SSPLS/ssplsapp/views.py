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
    games = Game.objects.exclude(secondbet='nb')
    context = {'games': games}
    return render(request, 'played-games.html', dict(context))
def availablegames(request):
    games = Game.objects.filter(secondbet='nb')
    context = {'games': games}
    return render(request, 'available-games.html', dict(context))
def statistics(request):
    playedGames = Game.objects.exclude(secondbet='nb')
    availableGames = Game.objects.filter(secondbet='nb')
    context = {'playedGames': playedGames, 'availableGames': availableGames}
    return render(request, 'statistics.html', dict(context))
def playgame(request, game_id):
    game = Game.objects.get(pk=game_id)
    context = {'game': game}
    return render(request, 'play-game.html', dict(context))
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
def gamerusult(firstbet, secondbet):
    result = ""
    if firstbet == secondbet:
        result == "draw"
    elif firstbet == 'stone':
        if secondbet == 'lizard':
            result = "firstwon"
        elif secondbet == "scissors":
            result == "firstwon"
        else:
            result == "secondwon"
    elif firstbet == "scissors":
        if secondbet == 'lizard':
            result = "firstwon"
        elif secondbet == "paper":
            result == "firstwon"
        else:
            result == "secondwon"
    elif firstbet == "paper":
        if secondbet == 'stone':
            result = "firstwon"
        elif secondbet == "spock":
            result == "firstwon"
        else:
            result == "secondwon"
    elif firstbet == "lizard":
        if secondbet == 'spock':
            result = "firstwon"
        elif secondbet == "paper":
            result == "firstwon"
        else:
            result == "secondwon"
    elif firstbet == "spock":
        if secondbet == 'scissors':
            result = "firstwon"
        elif secondbet == "stone":
            result == "firstwon"
        else:
            result == "secondwon"
    return result
