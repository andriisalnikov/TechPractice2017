from django.conf.urls import url

from polls.views import categories, competitions

urlpatterns = [
    url(r'^categories/all', categories.get_categories),
    url(r'^categories/create', categories.create_category),
    url(r'^competitions/create', competitions.create_competition),
    url(r'^competitions/all', competitions.get_competitions)
]
