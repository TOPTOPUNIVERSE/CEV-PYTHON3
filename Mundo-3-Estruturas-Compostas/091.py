# Guarde 4 resultados aleatórios de um dado em um dicionário depois coloque
# em ordem e mostre a classificação sendo o 1 lugar o maior número sorteado.

from random import randint
from time import sleep
from operator import itemgetter

print('-='*3, '    SORTEANDO OS VALORES    ', '-='*3)
jogo = {'1° Jogador': randint(1, 6),
        '2° jogador': randint(1, 6),
        '3° jogador': randint(1, 6),
        '4° jogador': randint(1, 6)}

ranking = []
for keys, values in jogo.items():
    print(f'{keys} tirou {values} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-'*40)
print('Ranking dos jogadores: ')
for indice, valores in enumerate(ranking):
    print(f'{indice+1}° lugar: {valores[0]} com {valores[1]}')
    sleep(1)
print('-='*3, '    FIM    ', '-='*3)
