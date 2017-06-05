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
        ('stone', 'stone'),
        ('scissors', 'scissors'),
        ('paper', 'paper'),
        ('lizard', 'lizard'),
        ('spock', 'spock'),
    )
    SECONDBET = (
        ('nb', ''),
        ('stone', 'stone'),
        ('scissors', 'scissors'),
        ('paper', 'paper'),
        ('lizard', 'lizard'),
        ('spock', 'spock'),
    )
    STATUS = (
        ('np', ''),
        ('firstwon', 'firstwon'),
        ('secondwon', 'secondwon'),
        ('draw', 'draw'),
    )
    firstbet = models.CharField(max_length=10, choices=FIRSTBET,default='')
    secondbet = models.CharField(max_length=10, choices=SECONDBET,default='')
    status = models.CharField(max_length=10, choices=STATUS,default='')