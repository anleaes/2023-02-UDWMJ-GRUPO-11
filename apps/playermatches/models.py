from django.db import models
from matches.models import Match
from players.models import Player

# Create your models here.

class PlayerMatch(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Jogador em Partida'
        verbose_name_plural = 'Jogadores em Partidas'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.total_price) 
