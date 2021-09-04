"""
Desafio 032
Problema: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

from datetime import date
y = int(input('Que ano você quer analisar? Coloque  0 para analisar o ano atual: '))
if y == 0:
    y == date.today().year
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print(f'O ano {y} é BISSEXTO')
else:
    print(f'O ano {y} não é BISSEXTO')
