from mongoengine import *


class Category(Document):
    id = SequenceField()
    name = StringField(max_length=200)
