from django.shortcuts import render
from .models import Jogo

def index(request):
    jogos_futebol = Jogo.objects.filter(modalidade__iexact='futebol')

    context = {
        'jogos_futebol': jogos_futebol,
    }
    return render(request, 'index.html', context)
