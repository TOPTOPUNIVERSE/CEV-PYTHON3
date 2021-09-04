"""
Desafio 003
Problema: Crie um programa que leia dois números e mostre a soma entre eles."""
# Solicitando um número
n1 = int(input('Digite um número:\033[1;34m '))
# Solicitando outro número
n2 = int(input('\033[mDigite outro número:\033[1;32m  '))
# Variável de soma dos números inseridos
s = n1+n2
# Mostrando na tela o resultado da soma
print(f'\033[mA soma entre  \033[1;34m{n1}\033[m e \033[1;32m{n2}\033[m é igual a {s}')
