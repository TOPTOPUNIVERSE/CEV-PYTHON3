"""
Desafio 031
Problema: Desenvolva um programa que pergunte a distância de
          uma viagem em Km. Calcule o preço da passagem, cobrando
          R$0,50 por Km para viagens de até 200Km e R$0,45 para
          viagens mais longas."""

from time import sleep
print('-='*10, 'Calcule sua viagem', '-='*10)
km = float(input('Qual é a distância da sua viagem? '))
print('Calculando...')
sleep(1)
p = km * 0.50 if km <= 200 else km * 0.45
print(f'Você está prestes a começar uma viagem de {km}km.')
print(f'Sua viagem custará R${p:.2f}')
print('-='*6, 'Obrigado por usar nossa calculadora', '-='*6)
