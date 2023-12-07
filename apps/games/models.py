from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField('Nome', max_length=50)
    genre = models.CharField('Genero', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering =['id']

    def __str__(self):
        return self.name