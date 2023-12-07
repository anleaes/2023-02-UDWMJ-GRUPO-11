from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlayerMatchForm
from .models import PlayerMatch, Match, Player

# Create your views here.

def add_playermatch(request, id_player):
    template_name = 'playermatches/add_playermatch.html'
    context = {}
    if request.method == 'POST':
        form = PlayerMatchForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.player = Player.objects.get(id=id_player)
            f.save()
            form.save_m2m()
            return redirect('playermatches:list_playermatches')
    form = PlayerMatchForm()
    context['form'] = form
    return render(request, template_name, context)

def list_playermatches(request):
    template_name = 'playermatches/list_playermatches.html'
    playermatches = PlayerMatch.objects.filter()
    matches = Match.objects.filter()
    players = Player.objects.filter()
    context = {
        'playermatches': playermatches,
        'matches': matches,
        'players': players
    }
    return render(request, template_name, context)

def delete_playermatch(request, id_playermatch):
    playermatch = PlayerMatch.objects.get(id=id_playermatch)
    playermatch.delete()
    return redirect('playermatches:list_playermatches')

def edit_playermatch_status(request, id_playermatch):
    template_name = 'playermatches/edit_playermatch_status.html'
    context ={}
    playermatch = get_object_or_404(PlayerMatch, id=id_playermatch)
    if request.method == 'POST':
        form = PlayerMatchForm(request.POST, instance=playermatch)
        if form.is_valid():
            form.save()
            return redirect('playermatches:list_playermatches')
    form = PlayerMatchForm(instance=playermatch)
    context['form'] = form
    return render(request, template_name, context)