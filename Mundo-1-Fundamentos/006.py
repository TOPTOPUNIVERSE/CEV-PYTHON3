"""
Desafio 006
Problema: Crie um algoritmo que leia um número e mostre o seu drobro,
          triplo e raiz quadrada."""

# Solicitando número
n = int(input('Digite um número:\033[1;31m '))
# Mostrando na tela o dobro o triplo e a raíz quadrada do número inserido
print(f'\033[mO dobro de \033[1;31m{n}\033[m é \033[1;97m{n*2}\033[m\nO triplo de \033[1;31m{n}\033[m é \033[1;97m{n*3}\033[m\nE a raiz quadrada de \033[1;31m{n}\033[m é \033[1;97m{n**(1/2):.2f}\033[m')
#
# Para dar a cor vermelha ao número inserido:\033[1;31m \033[m
# Para dar a cor branca ao número computado: \033[1;97m \033[m
