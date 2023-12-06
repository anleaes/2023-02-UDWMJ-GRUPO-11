from django.db import models
from items.models import Item


# Create your models here.

class Player(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    email = models.EmailField('E-mail',null=False, blank=False)
    
# ESPAÇO PARA CLASSE INVENTORY

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
        ordering =['id']

    def __str__(self):
        return self.first_name

# ESPAÇO PARA CLASSE INVENTORY
