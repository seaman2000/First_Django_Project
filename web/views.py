from django.shortcuts import render, redirect
from .models import Match

def home(request):
    if request.method == 'POST':
        home_team = request.POST.get('home_team')
        away_team = request.POST.get('away_team')
        odds = request.POST.get('odds')

        Match.objects.create(
            home_team=home_team,
            away_team=away_team,
            odds=odds,
        )

        return redirect('home')

    matches = Match.objects.all()

    return render(request, 'home.html', {'matches': matches})