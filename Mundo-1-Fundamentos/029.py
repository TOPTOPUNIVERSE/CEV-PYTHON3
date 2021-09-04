
"""
Desafio 029
Problema: Escreva um programa que leia a velocidade de um carro.
          Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
          que ele foi multado. A multa vai custar R$7,00 por cada
          Km acima do limite."""

from time import sleep  # Traz a variavel de sleep
print('>'*10, 'Radar fast furious', '<'*10)
vo = float(input('Qual a velocidade em Kms por hora?  '))
m = (vo - 80) * 7  # Calculo da multa
print('Analisando...')
sleep(1)  # Dar a ideia de que o programa está pensando
if vo > 80:
    print(f'Veloses e Furiosos é ??\n Toma multa então R${m:.2f}')  # .2f para mostrar somente duas casas após a virgula
else:
    print('Muito bom !\nContinue respeitando o limite de velocidade.')
print('>'*6, 'Dirija com cuidado sempre', '<'*6)
