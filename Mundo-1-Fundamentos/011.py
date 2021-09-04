"""
Desafio 011
Problema: Faça um programa que leia a largura e a altura de uma
          parede em metros, calcule a sua área e a quantidade de
          tinta necessária para pintá-la, sabendo que cada litro
          de tinta pinta uma área de 2 metros quadrados"""

l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
ar = l * a
print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de: {ar}m².')
lt = ar/2
print(f'Você precisa de: {lt}l de tinta.')
