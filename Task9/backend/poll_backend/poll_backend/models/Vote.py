from mongoengine import *;
from poll_backend.models import Competitor, Category, Voter


class Vote(Document):
    competitor = ReferenceField(Competitor)
    category = ReferenceField(Category)
    voter = ReferenceField(Voter)
