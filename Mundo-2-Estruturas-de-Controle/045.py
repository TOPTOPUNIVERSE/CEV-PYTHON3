#Importando a biblioteca de aleatóriedade
from random import randint
#Importando a biblioteca de tempo
from time import sleep
#Cabeçalho do programa
print('-='* 10, 'Jokenpô', '-='*10)
#Opções do computador
itens = ('Pedra', 'Papel', 'Tesoura')
#Solicitando sorteio das opções
pc = randint(0, 2)
#Mostrando na tela qual opção foi sorteada
#print(f'O computador escolheu {itens[pc]}')
#Variavel para escolha do player
print (''' Suas opções:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
player = int(input('Qual é a sua escolha? ')) 
print('JO')
sleep (1)
print('KEN')
sleep (1)
print('PÔ!')
sleep (1)
print('>'* 55)
if pc == 0: #PC jogou PEDRA
    if player == pc: #Se ambos jogarem a mesma opção
        print(f'Deu EMPATE!\nO computador escolheu {itens[pc]}'
                f' e você escolheu {itens[player]}.')
    elif player == 1:
        print(f'Você VENCEU!!\nO computador escolheu {itens[pc]} '
            f' e você escolheu {itens[player]}.')
    elif player == 2:
        print(f'Você PERDEU!\nO computador escolheu {itens[pc]}'
              f' e você escolheu {itens[player]}.')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1: #PC jogou PAPEL
    if player == 0: #Player jogou PEDRA
        print(f'Você PERDEU!\nO computador escolheu {itens[pc]}'
              f' e você escolheu {itens[player]}.')
    elif player == pc:
        print(f'Deu EMPATE!\nO computador escolheu {itens[pc]}'
              f' e você escolheu {itens[player]}.')
    elif player == 2:
        print(f'Você VENCEU!!\nO computador escolheu {itens[pc]}'
              f' e você escolheu {itens[player]}.')
    else:
        print('JOGADA INVÁLIDA!')
else: #PC jogou TESOURA
    if player == 0:
        print(f'Você VENCEU!!\nO computador escolheu {itens[pc]}'
              f' e você escolheu {itens[player]}.')
    elif player == 1:
        print(f'Você PERDEU!\nO computador escolheu {itens[pc]}'
              f' e você escolheu {itens[player]}.')
    elif player == pc:
        print(f'Deu EMPATE\nO computador escolheu {itens[pc]}'
               f' e você escolheu {itens[pc]}.')
    else:
        print('JOGADA INVÁLIDA!')
print('<'*55)
print('-='*10, 'END', '-='*10)
