"""
Desafio 017
Problema: Faça um programa que leia o comprimento do cateto oposto e
          do cateto adjacente de um triângulo retângulo. Calcule e
          mostre o comprimento da hipotenusa."""


co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co**2 + ca**2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')  # maneira matematica sem importação
#import math

'''import math
cco = float(input('Qual o comprimento do cateto oposto:'))
cca = float(input('Qual o comprimeento do cateto adjacente:'))
print(f'A hipotenusa é {math.hypot(cca,cco)}')'''
