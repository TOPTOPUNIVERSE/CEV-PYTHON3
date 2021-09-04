"""
Desafio 024
Problema: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"."""

# Solicitando a cidade de nascimento
c = str(input('Em que cidade você nasceu?\033[1;33m  ')).strip()
# Mostrando na tela se a cidade tem santo no nome
print('\033[m', c[:5].upper() == 'SANTO')
#
# Para cor amarela do nome da cidade inserida: \033[1;33m
