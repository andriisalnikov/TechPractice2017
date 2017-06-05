"""SSPLS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from ssplsapp.views import index, playedgames, availablegames, statistics, playgame, creategame, game, addgame

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addgame/', addgame),
    url(r'^$', index),
    url(r'^played-games/', playedgames),
    url(r'^available-games/', availablegames),
    url(r'^statistics/', statistics),
    url(r'^play-game\/[1-9][0-9]*/', playgame),
    url(r'^create-game/', creategame),
    url(r'^game\/[1-9][0-9]*/', game),
]
