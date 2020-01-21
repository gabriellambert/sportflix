# Generated by Django 3.0.2 on 2020-01-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jogador_01', models.CharField(max_length=50)),
                ('jogador_02', models.CharField(max_length=50)),
                ('torneio', models.CharField(max_length=100)),
                ('ano', models.CharField(max_length=4)),
                ('modalidade', models.CharField(choices=[('FUT', 'futebol'), ('BAS', 'basquete'), ('TEN', 'tenis')], max_length=3)),
                ('imagem', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y')),
            ],
        ),
    ]
