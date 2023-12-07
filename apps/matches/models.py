from django.db import models
from games.models import Game

# Create your models here.

class Match(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    day = models.CharField('Dia', max_length=50)
    hour = models.CharField('Hora', max_length=50)
    
    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'
        ordering =['id']

    def __str__(self):
        return self.game