from mongoengine import *


class Competitor(Document):
    id = SequenceField()
    firstName = StringField(max_length=200)
    lastName = StringField(max_length=200)
    course = IntField(min_value=1, max_value=6)
    speciality = StringField(max_length=100)
