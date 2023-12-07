from django.db import models
from games.models import Game

# Create your models here.

class Match(models.Model):
    jogo = models.CharField('Jogo', max_length=50)
    dia = models.CharField('Dia', max_length=50)
    hora = models.CharField('Hora', max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'
        ordering =['id']

    def __str__(self):
        return self.name