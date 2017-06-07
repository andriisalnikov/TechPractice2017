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
    if request.user.is_anonymous:
        return  redirect('/')
    else:
        auth.logout(request)
        context_data = ""
        return render(request, 'index.html', dict(context_data))
def index(request):
    context_data = ""
    return render(request, 'index.html', dict(context_data))
def playedgames(request):
    if request.user.is_anonymous:
        return HttpResponse('<h1>You are not logined</h1> <a href="/">Main page</a>')
    else:
        games = Game.objects.exclude(secondbet='nb')
        context = {'games': games}
        return render(request, 'played-games.html', dict(context))
def availablegames(request):
    if request.user.is_anonymous:
        return HttpResponse('<h1>You are not logined</h1> <a href="/">Main page</a>')
    else:
        games = Game.objects.filter(secondbet='nb')
        if User.objects.filter(username=request.user.username).count() == 0:
            u3 = User(username=request.user.username)
            u3.save()
            user = u3
        else:
            user = User.objects.get(username=request.user.username)
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
    if request.user.is_anonymous:
        return HttpResponse('<h1>You are not logined</h1> <a href="/">Main page</a>')
    else:
        playedGames = Game.objects.exclude(secondbet='nb')
        availableGames = Game.objects.filter(secondbet='nb')
        bestPlayer = User.objects.raw('select u.id, count(g.id) as allgames from ssplsapp_user as u LEFT JOIN ssplsapp_game as g on g.firstuser_id=u.id and g.status = "firstwon" LEFT JOIN ssplsapp_game as g2 on g2.seconduser_id=u.id and g2.status = "secondwon" GROUP BY u.id ORDER BY allgames DESC')
        games1 = Game.objects.filter(firstuser=bestPlayer[0]).count()
        games2 = Game.objects.filter(seconduser=bestPlayer[0]).count()
        bestUserGames = games1 + games2
        games1 = Game.objects.filter(firstuser=bestPlayer[0],status='firstwon').count()
        games2 = Game.objects.filter(seconduser=bestPlayer[0],status='secondwon').count()
        bestWonGames = games1 + games2
        worstPlayer = User.objects.raw('select u.id, count(g.id) as allgames from ssplsapp_user as u LEFT JOIN ssplsapp_game as g on g.firstuser_id=u.id and g.status = "secondwon" LEFT JOIN ssplsapp_game as g2 on g2.seconduser_id=u.id and g2.status = "firstwon" GROUP BY u.id ORDER BY allgames DESC')
        games1 = Game.objects.filter(firstuser=worstPlayer[0]).count()
        games2 = Game.objects.filter(seconduser=worstPlayer[0]).count()
        worstUserGames = games1 + games2
        games1 = Game.objects.filter(firstuser=worstPlayer[0],status='secondwon').count()
        games2 = Game.objects.filter(seconduser=worstPlayer[0],status='firstwon').count()
        worstLooseGames = games1 + games2
        context = {'playedGames': playedGames, 'availableGames': availableGames, 'bestPlayer': bestPlayer, 'bestUserGames': bestUserGames, 'bestWonGames': bestWonGames, 'worstUserGames': worstUserGames, 'worstLooseGames': worstLooseGames, 'worstPlayer': worstPlayer}
        return render(request, 'statistics.html', dict(context))
def playgame(request, game_id):
    if request.user.is_anonymous:
        return HttpResponse('<h1>You are not logined</h1> <a href="/">Main page</a>')
    else:
        game = Game.objects.get(pk=game_id)
        context = {'game': game}
        return render(request, 'play-game.html', dict(context))
def creategame(request):
    if request.user.is_anonymous:
        return HttpResponse('<h1>You are not logined</h1> <a href="/">Main page</a>')
    else:
    	context_data = ""
    	return render(request, 'create-game.html', dict(context_data))
def game(request):
    if request.user.is_anonymous:
        return HttpResponse('<h1>You are not logined</h1> <a href="/">Main page</a>')
    else:
    	context_data = ""
    	return render(request, 'game-result.html', dict(context_data))
def addgame(request):
    if request.user.is_anonymous:
        return HttpResponse('<h1>You are not logined</h1> <a href="/">Main page</a>')
    else:
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
    if request.user.is_anonymous:
        return HttpResponse('<h1>You are not logined</h1> <a href="/">Main page</a>')
    else:
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
