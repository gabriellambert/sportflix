from django.db import models

MODALIDADE_CHOICES = [
    ('FUT', 'futebol'),
    ('BAS', 'basquete'),
    ('TEN', 'tenis'),
]

class Jogo(models.Model):
    jogador_01 = models.CharField(max_length=50)
    jogador_02 = models.CharField(max_length=50)
    torneio = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    modalidade = models.CharField(choices=MODALIDADE_CHOICES, max_length=3)
    imagem = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
