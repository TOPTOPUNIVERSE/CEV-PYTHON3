"""
Desafio 028
Problema: Escreva um programa que faça o computador "pensar"
          em um número inteiro entre 0 e 5 e peça para o usuário
          tentar descobrir qual foi o número escolhido pelo computador.
          O programa deverá escrever na tela se o usuário venceu ou perdeu."""

# Importando função randint da biblioteca random
from random import randint
# Importando função sleep da biblioteca time
from time import sleep
# Variável que faz o código sortear um número de 0 a 5
r = randint(0, 5)
# Mostrando na tela cabeçalho do programa
print('-='*10, 'Jogo da adivinhação ', '-='*10)
# Solicitando que o jogador adivinhe um número de 0 á 5
q = int(input('Estou pensando em um número de 0 a 5, consegue adivinhar?  '))
# Mostrando na tela a mensagem 'Processando...' passando o conceito de vida em máquina
print('Processando...')
# Colocando o programa para descansar por 2 segundos
sleep(2)
# Se o número inserido for igual ao número sorteado
if q == r:
    # Mostre na tela 'Caramba você é um bom adivinho !!'
    print('Acertou ! ! !\nCaramba você é um bom adivinho !!')
# Caso contrário
else:
    # Mostre na tela'Hmmm... não foi esse o número emm'....
    print(f'Hmmm... não foi esse o número emm\nKkkkkkk vai ter que se esforçar mais.\nO número que pensei foi {r}')
# Mostre na tela o cabeçalho de fim de jogo
print('-='*12, 'END GAME', '-='*12)
#
