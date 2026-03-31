from django.shortcuts import render

def home(request):
    context = {
        'name': 'Георги',
        'message': 'Това е динамично съдържание 😎'
    }
    return render(request, 'home.html', context)