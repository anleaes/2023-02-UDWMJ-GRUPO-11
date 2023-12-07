from django.db import models
from matches.models import Match
from players.models import Player

# Create your models here.

class PlayerMatch(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')

    class Meta:
        verbose_name = 'Jogador em Partida'
        verbose_name_plural = 'Jogadores em Partidas'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.player) 

class PlayerMatchItem(models.Model):
    playermatch = models.ForeignKey(PlayerMatch, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)

    class Meta:
        verbose_name = 'Partida do Jogador'
        verbose_name_plural = 'Partidas do Jogador'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.playermatch) 