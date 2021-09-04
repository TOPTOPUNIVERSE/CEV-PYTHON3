"""
Desafio 007
Problema: Desenvolva um programa que leia as duas notas de um aluno,
          calcule e mostre a sua média."""

# Solicitando a nota geral
n = float(input('Digite sua nota geral:\033[1;33m '))
# Solicitando a nota da redação
n1 = float(input('\033[mDigite a nota da redação:\033[1;94m '))
# Mostrando na tela a média final
print(f'\033[mA média entre {n} e {n1} é: \033[1;32m{(n+n1)/2:.1f}\033[m')
#
# Para dar cor amarela na  nota geral, utilizamos: \033[1;93m
# Para dar cor azul claro na nota da redação, utilizamos: \033[1;94m
# Para dar cor verde na média final, utilizamos: \033[1;32m
