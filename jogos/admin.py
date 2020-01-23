from django.contrib import admin
from .models import Jogo


class ApresentandoJogos(admin.ModelAdmin):
    list_display = ('__str__', 'torneio', 'ano', 'modalidade')
    list_per_page = 10
    search_fields = ('jogador_01', 'jogador_02', )
    list_filter = ('modalidade', 'ano', 'torneio', )

admin.site.register(Jogo, ApresentandoJogos)
