"""
Desafio 030
Problema:  Crie um programa que leia um número inteiro e 
mostre na tela se ele é PAR ou ÍMPAR."""

from time import sleep
print('~'*6, 'Bora ver se esse número ai é par ???', '~'*6)
n = int(input('Dígite um número qualquer: '))
print('Hmmmmmm...Éeeeee')
sleep(1)
p = n % 2  # A porcentagem nos indica o resto da divisão do n por 2
if p == 0:  # Lembre-se igual em python é duas vezes o sinal de igual
    print('\nPAR')
else:
    print('\nÍMPAR')

print('~'*6, 'ParouÍmpar', '~'*6)
