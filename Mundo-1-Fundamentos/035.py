"""
Desafio 035
Problema: Desenvolva um programa que leia o comprimento de três
          retas e diga ao usuário se elas podem ou não formar um triângulo."""


print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))  # Colocando o segmento 1
r2 = float(input('Segundo segmento: '))  # Colocando o segmento 2
r3 = float(input('Terceiro segmento: '))  # Colocando o segmento 3
if r1 <= r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos PODEM formar um triângulo.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
