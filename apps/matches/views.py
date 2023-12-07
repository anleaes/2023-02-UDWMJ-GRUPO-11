from django.shortcuts import render, get_object_or_404, redirect
from .forms import MatchForm
from .models import Match

# Create your views here.

def add_match(request):
    template_name = 'matches/add_match.html'
    context = {}
    if request.method == 'POST':
        form = MatchForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('matches:list_matches')
    form = MatchForm()
    context['form'] = form
    return render(request, template_name, context)

def list_matches(request):
    template_name = 'matches/list_matches.html'
    matches = Match.objects.filter()
    context = {
        'matches': matches
    }
    return render(request, template_name, context)

def edit_match(request, id_match):
    template_name = 'matches/add_match.html'
    context ={}
    match = get_object_or_404(Match, id=id_match)
    if request.method == 'POST':
        form = MatchForm(request.POST, request.FILES,  instance=match)
        if form.is_valid():
            form.save()
            return redirect('matches:list_matches')
    form = MatchForm(instance=match)
    context['form'] = form
    return render(request, template_name, context)

def delete_match(request, id_match):
    match = Match.objects.get(id=id_match)
    match.delete()
    return redirect('matches:list_matches')
