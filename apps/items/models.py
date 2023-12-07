from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField('Nome', max_length=50)
    element = models.CharField('Elemento', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    TYPE_CHOICES = (
        ('ARM', 'Arma'),
        ('ARD', 'Armadura'),
        ('CON', 'Consumivel'),
    )
    type = models.CharField('Tipo', max_length=3, choices=TYPE_CHOICES)    
    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
        ordering =['id']

    def __str__(self):
        return self.name
    