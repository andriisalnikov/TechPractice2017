from mongoengine import *


class Voter(Document):
    id: SequenceField()
    socialId: StringField()
    socialType: IntField(min_value=1, max_value=3)
