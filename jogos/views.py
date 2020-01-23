from django.shortcuts import render
from .models import Jogo

def index(request):
    jogos_futebol = Jogo.objects.filter(modalidade='FUT')[:4]
    jogos_basquete = Jogo.objects.filter(modalidade='BAS')[:4]
    jogos_tenis = Jogo.objects.filter(modalidade='TEN')[:4]
    context = {
        'jogos_futebol': jogos_futebol,
        'jogos_basquete': jogos_basquete,
        'jogos_tenis': jogos_tenis,
    }
    return render(request, 'index.html', context)
