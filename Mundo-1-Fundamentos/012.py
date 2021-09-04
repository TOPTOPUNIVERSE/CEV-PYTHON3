"""
Desafio 012
Problema: Faça um algoritmo que leia o preço de um produto e
          mostre seu novo preço, com 5% de desconto."""

# Solicitando o valor do produto
po = float(input('Quanto tá:\033[1;31m R$'))
# Variável da lógica de porcentagem
# 1500*5/100 < tudo isso menos o valor original :)
pd = po-(po * 5 / 100)
# Mostrando na tela o valor do produto com 5% de desconto
print(f'\033[mNovo valor com 5% de desconto:\033[1;32m R${pd:.2f}\033[m')
#
# Para cor vermelha do preço original: \033[1;31m
# Para cor verde do novo preço com desconto: \033[1;32m
