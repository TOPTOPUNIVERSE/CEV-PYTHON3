"""
Desafio 013
Problema: Faça um algoritmo que leia o salário de um funcionário
          e mostre seu novo salário, com 15% de aumento."""

# Solicitando o salário atual
so = float(input('Salário atual:\033[1;31m R$'))
# Variável de porcentagem de aumento
sf = so + (so * 15 / 100)
# Mostrando na tela o salário com 15% de aumento
print(f'\033[mSalário com 15% de aumento:\033[1;32m R${sf:.2f}\033[m')
#
# Para cor vermelha do salário atual: \033[1;31m
# Para cor verde do salário com 15% de aumento: \033[1;32m
