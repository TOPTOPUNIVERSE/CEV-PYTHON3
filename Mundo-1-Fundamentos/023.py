"""
Desafio 023
Problema: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Solicitando um número de 0 a 9999"""

n = int(input('Digite um número de 0 a 9999:\033[1;31m '))
# Variável para unidade
u = n // 1 % 10
# Variável para dezena
d = n // 10 % 10
# Variável para centena
c = n // 100 % 10
# Variável para milhar
m = n // 1000 % 10
# Mostrando na tela a unidade, a dezena, a centena e a unidade
# de milhar do número inserido
print(
    f'\033[m\033[1;34mUnidade: {u}\033[m\n\033[1;32mDezena: {d}\033[m\n\033[1;33mCentena: {c}\033[m\n\033[1;36mMilhar: {m}\033[m')
#
# Para a cor vermelha no número inserido: \033[1;31m
# Para a cor azul na unidade: \033[1;34m
# Para a cor verde na dezena: \033[1;32m
# Para a cor amarela na centena: \033[1;33m
# Para a cor cyan na unidade de milhar: \033[1;36m
