from django.shortcuts import render
from .models import Game
from django.http import HttpResponse

# Create your views here.
def simple_view(request):
    return HttpResponse('Hello')

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_detail(request, game_id):
    game = Game.objects.get(pk=game_id)
    return render(request, 'games/game_detail.html', {'game': game})
