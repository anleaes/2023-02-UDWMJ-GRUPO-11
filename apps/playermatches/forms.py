from django import forms
from .models import PlayerMatch, Player, PlayerMatchItem, Match

class PlayerMatchForm(forms.ModelForm):
    
    class Meta:
        model = PlayerMatch
        exclude = ('player', 'created_on' , 'updated_on')

class PlayerMatchItemForm(forms.ModelForm):
        
    class Meta:
        model = PlayerMatchItem
        exclude = ('playermatch', 'created_on' , 'updated_on')
