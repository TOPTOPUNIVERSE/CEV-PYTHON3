
"""
Desafio 033
Problema: Faça um programa que leia três números e mostre qual é o maior
 e qual é o menor."""


# Solicitando número de 1 á 10
n = int(input('Digite um número de 1 á 10: '))
# Solicitando mais um número de 1 á 10
n1 = int(input('Digite mais um número de 1 á 10: '))
# Solicitando outro número de 1 á 10
n2 = int(input('Digite outro número de 1 á 10: '))
# Variável para verificar quem é o menor número dos 3 digitados
s = n
# Se o 1° número for menor que o número 0 e
# O número 1° for menor que o número 2
if n1 < n and n1 < n2:
    # Então o menor número será o número 1°
    s = n1
# Se o 2° número for menor que o número 0 e
# O número 2 for menor que o número 1°
if n2 < n and n2 < n1:
    # Então o menor número é o número 2
    s = n2
# Variável para verificar quem é o maior
l = n
# Se o número 1 é maior que o número 0 e
# O número 1 é maior que o número 2
if n1 > n and n1 > n2:
    # Então o maior número é o número 1
    l = n1
# Se o 2° número é maior que o número 0 e
# O número 2 é maior que o número 1
if n2 > n and n2 > n1:
    # Então o número 2 é o maior
    l = n2
# Mostre na tela o maior número digitado e
# O menor número digitado
print(f'O maior número digitado foi:\033[1;32m {l}\033[m\nO menor número digitado foi:\033[1;31m {s}\033[m')
#
# Para cor verde no maior número: \033[1;32m
# Para cor vermelha no menor número: \033[1;31m
