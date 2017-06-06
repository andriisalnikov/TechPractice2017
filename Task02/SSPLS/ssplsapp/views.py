from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.contrib import auth
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.loader import get_template
from django.template import Context
from .forms import ContactForm
from .models import Game, User

def logout(request):
    auth.logout(request)
    context_data = ""
    return render(request, 'index.html', dict(context_data))
def index(request):
    context_data = ""
    return render(request, 'index.html', dict(context_data))
def playedgames(request):
    games = Game.objects.exclude(secondbet='nb')
    context = {'games': games}
    return render(request, 'played-games.html', dict(context))
def availablegames(request):
    games = Game.objects.filter(secondbet='nb')
    user = User.objects.get(username=request.user)
    games1 = Game.objects.filter(firstuser=user).count()
    games2 = Game.objects.filter(seconduser=user).count()
    userGames = games1 + games2
    games1 = Game.objects.filter(firstuser=user,status='firstwon').count()
    games2 = Game.objects.filter(seconduser=user,status='secondwon').count()
    wonGames = games1 + games2
    games1 = Game.objects.filter(firstuser=user,status='secondwon').count()
    games2 = Game.objects.filter(seconduser=user,status='firstwon').count()
    lostGames = games1 + games2
    games1 = Game.objects.filter(firstuser=user,status='draw').count()
    games2 = Game.objects.filter(seconduser=user,status='draw').count()
    drawnGames = games1 + games2
    context = {'games': games, 'userGames': userGames, 'wonGames': wonGames, 'lostGames': lostGames, 'drawnGames': drawnGames}
    return render(request, 'available-games.html', dict(context))
def statistics(request):
    playedGames = Game.objects.exclude(secondbet='nb')
    availableGames = Game.objects.filter(secondbet='nb')
    bestPlayer = User.objects.raw('select * from ssplsapp_user WHERE id=1')
    context = {'playedGames': playedGames, 'availableGames': availableGames, 'bestPlayer': bestPlayer}
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
def addgame(request):
    context_data = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            bet = form.cleaned_data['bet']
            user = request.user
            #вставка в базу
            if User.objects.filter(username = user).count() > 0:
                u1 = User.objects.get(username=user)
            else:
                u3 = User(username=user)
                u3.save()
                u1 = u3
            u2 = User.objects.get(username='np')
            g = Game(firstuser=u1,seconduser=u2,firstbet=bet,secondbet='nb',status='np')
            g.save()
            return  redirect('/available-games')
        else:
            return HttpResponse('invalid')
    else:
        form = ContactForm()
    #Выводим форму в шаблон
    return HttpResponse('nopost')
def play(request, game_id):
    context_data = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            bet = form.cleaned_data['bet']
            game = Game.objects.get(pk=game_id)
            user = request.user
            #вставка в базу
            if User.objects.filter(username = user).count() > 0:
                u1 = User.objects.get(username=user)
            else:
                u3 = User(username=user)
                u3.save()
                u1 = u3
            status = gameresult(game.firstbet, bet)
            game.seconduser = u1
            game.secondbet = bet
            game.status = status
            game.save()
            return  redirect('/available-games')
        else:
            return HttpResponse('invalid')
    else:
        form = ContactForm()
    #Выводим форму в шаблон
    return HttpResponse('nopost')
def gameresult(firstbet, secondbet):
    result = ""
    if firstbet == secondbet:
        result = "draw"
    elif firstbet == 'stone':
        if secondbet == 'lizard':
            result = "firstwon"
        elif secondbet == "scissors":
            result = "firstwon"
        else:
            result = "secondwon"
    elif firstbet == "scissors":
        if secondbet == 'lizard':
            result = "firstwon"
        elif secondbet == "paper":
            result = "firstwon"
        else:
            result = "secondwon"
    elif firstbet == "paper":
        if secondbet == 'stone':
            result = "firstwon"
        elif secondbet == "spock":
            result = "firstwon"
        else:
            result = "secondwon"
    elif firstbet == "lizard":
        if secondbet == 'spock':
            result = "firstwon"
        elif secondbet == "paper":
            result = "firstwon"
        else:
            result = "secondwon"
    elif firstbet == "spock":
        if secondbet == 'scissors':
            result = "firstwon"
        elif secondbet == "stone":
            result = "firstwon"
        else:
            result = "secondwon"
    return result
