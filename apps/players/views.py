from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlayerForm
from .models import Player, Item

# IMPORTE A CLASSE INVENTORY ACIMA!



def add_player(request):
    template_name = 'players/add_player.html'
    context = {}
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('players:list_players')
    form = PlayerForm()
    context['form'] = form
    return render(request, template_name, context)



# ESPAÇO PARA SCRIPT DA CLASSE INVENTORY!



def edit_player(request, id_player):
    template_name = 'players/add_player.html'
    context ={}
    player = get_object_or_404(Player, id=id_player)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('players:list_players')
    form = PlayerForm(instance=player)
    context['form'] = form
    return render(request, template_name, context)

def delete_player(request, id_player):
    player = Player.objects.get(id=id_player)
    player.delete()
    return redirect('players:list_players')
