from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.loader import get_template
from django.template import Context
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