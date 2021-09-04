
"""
Desafio 018
Problema: Faça um programa que leia um ângulo qualquer e mostre na
          tela o valor do seno, cosseno e tangente desse ângulo."""

# Importando a biblioteca de matemática
import math
# Solicitando o ângulo
a = float(input('Qual é o ângulo?\033[1;37m '))
# Variável para o seno do ângulo
s = math.sin(math.radians(a))
# Mostrando na tela o valor do seno
print(f'\033[mO seno de \033[1;37m{a}° graus\033[m é \033[1;96m{s:.2f}°\033[m')
# Variável para o cosseno do ângulo
c = math.cos(math.radians(a))
# Mostrando na tela o cosseno do ângulo
print(f'O cosseno de \033[1;37m{a}° graus\033[m é \033[1;96m{c:.2f}°\033[m')
# Variável para tangente do ângulo
t = math.tan(math.radians(a))
# Mostrando na tela a tangente do ângulo
print(f'A tangente de \033[1;37m{a}° graus\033[m é \033[1;96m{t:.2f}°\033[m')
#
# Para a cor cinza claro do valor inserido e do grau: \033[1;37m
# Para a cor  cyan claro dos números computados: \033[1;96m
