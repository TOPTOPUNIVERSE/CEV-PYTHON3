
"""
Desafio 015
Problema: Escreva um programa que pergunte a quantidade de Km
          percorridos por um carro alugado e a quantidade de dias
          pelos quais ele foi alugado. Calcule o preço a pagar,
          sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

da = int(input('Aluguei o carro por quantos dias: '))
kr = float(input('Quantos Kms eu rodei: '))
vf = da * 60 + (kr * 0.15)
print(f'Você deve pagar R${vf:.2f}')
