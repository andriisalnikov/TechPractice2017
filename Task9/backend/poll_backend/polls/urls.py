from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^categories/all', views.get_categories),
    url(r'^categories/create', views.create_category)
]
