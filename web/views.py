from django.shortcuts import render, redirect
from .models import Match


def home(request):
    if request.method == 'POST':
        home_team = request.POST.get('home_team')
        away_team = request.POST.get('away_team')
        odds = request.POST.get('odds')
        match_date = request.POST.get('match_date')

        Match.objects.create(
            home_team=home_team,
            away_team=away_team,
            odds=odds,
            match_date=match_date,
        )

        return redirect('home')

    matches = Match.objects.all()
    return render(request, 'home.html', {'matches': matches})


def delete_match(request, id):
    match = Match.objects.get(id=id)
    match.delete()
    return redirect('home')