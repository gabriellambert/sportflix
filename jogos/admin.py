from django.contrib import admin
from .models import Jogo


class ApresentandoJogos(admin.ModelAdmin):
    list_display = ('__str__', 'torneio', 'ano', 'modalidade')

admin.site.register(Jogo, ApresentandoJogos)
