# Pergunte quantos jogos serão gerados, depois sorteie 6 números entre 1 e 60
# para cada jogo e  cadastre tudo em uma lista composta
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('    JOGA NA MEGA SENA    ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for indice, lista in enumerate(jogos):
    sleep(1)
    print(f'Jogo {indice+1}: {lista}')
print(f'-='*5, '< BOA SORTE! >', '-='*5)

'''minha solução
from random import randint
from time import sleep

sorteio = []
print('-='*15, 'JOGA NA MEGA SENA', '-='*15)
q = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*15, f'SORTEANDO {q} JOGOS', '-='*15)
for n in range(q):
    sorteio.clear()
    for c in range(1, 7):
        r = randint(1, 60)
        if r in sorteio:
            r = randint(1, 60)
            sorteio.append(r)
        else:
            sorteio.append(r)
        if len(sorteio) == 6:
            sorteio.sort()
            sleep(1)
            print(f'Jogo {n+1}: {sorteio}')
print('-='*15, 'BOA SORTE!', '-='*15)'''
