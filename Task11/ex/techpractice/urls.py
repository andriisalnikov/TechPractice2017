"""techpractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ex import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^validation/', views.validation, name='registration'),
    url(r'^myprofile/', views.myprofile, name='myprofile'),
    url(r'^create_fileset/', views.create_fileset, name='create_fileset'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^(?P<fileset_name>[0-9]+)/$', views.fileset, name='fileset'),
    url(r'^(?P<fileset_name>[0-9]+)/change_description', views.change_description, name='change_description'),
	url(r'^(?P<download_name>[0-9]+)/download/', views.download, name='download'),
    url(r'^(?P<fileset_name>[0-9]+)/change_description/', views.change_description, name='change_description'),
    url(r'^(?P<fileset_name>[0-9]+)/upload_file/', views.upload_file, name='upload_file')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
