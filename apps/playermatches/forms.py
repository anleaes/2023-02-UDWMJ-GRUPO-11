from django import forms
from .models import PlayerMatch, Player, Match

class PlayerMatchForm(forms.ModelForm):
    
    class Meta:
        model = PlayerMatch
        exclude = ('client', 'created_on' , 'updated_on')
