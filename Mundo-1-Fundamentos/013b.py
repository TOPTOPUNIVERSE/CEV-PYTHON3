"""
Desafio 013
Problema: Faça um algoritmo que leia o valor de um produto
          e mostre seu novo valor, com 12% de desconto e
          parcelado com 10% de juros."""
# Solicitando o valor do produto
vo = float(input('Valor do produto:\033[1;91m R$'))
# Variável de 12% de desconto
vd = vo - (vo * 12 / 100)
# Mostrando na tela o novo valor do produto com 12% de desconto
# (em casos de pagamento avista)
print(f'\033[mValor do produto com pagamento à vista ganha 12% de desconto:\033[1;32m R${vd:.2f}\033[m')
# Variável de 10% de juros(em caso de pagamentos com cartão)
vj = vo + (vo * 12 / 100)
# Mostrando na tela o valor com 10% de juros
print(f'Valor parcelado, com 10% de juros:\033[1;31m R${vj:.2f}\033[m')
#
# Para cor vermelha clara no valor do produto: \033[1;91m
# Para cor verde no valor do produto com 12% de desconto: \033[1;32m
# Para cor vermelha no valor do produto com 10% de juros: \033[1;31m
