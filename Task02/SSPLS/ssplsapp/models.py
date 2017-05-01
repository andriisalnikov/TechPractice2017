from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200,default='')
    def __str__(self):
        return self.username

class Game(models.Model):
    firstuser = models.ForeignKey(User, related_name='firstuser')
    seconduser = models.ForeignKey(User, related_name='seconduser')
    FIRSTBET = (
        ('st', 'stone'),
        ('sc', 'scissors'),
        ('p', 'paper'),
        ('l', 'lizard'),
        ('sp', 'spock'),
    )
    SECONDBET = (
        ('st', 'stone'),
        ('sc', 'scissors'),
        ('p', 'paper'),
        ('l', 'lizard'),
        ('sp', 'spock'),
    )
    firstbet = models.CharField(max_length=2, choices=FIRSTBET,default='')
    secondbet = models.CharField(max_length=2, choices=SECONDBET,default='')