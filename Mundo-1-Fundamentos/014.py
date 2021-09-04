"""
Desafio 014
Problema: Escreva um programa que converta uma temperatura
          digitando em graus Celsius e converta para graus Fahrenheit."""

# Solicitando valor da temperatura em °C
c = float(input('Temperatura atual em C°:\033[1;34m'))
# Variável de conversão de celsius para fahrenheit
f = ((9 * c) / 5) + 32
# Mostrando na tela a temperatura em Celsius e Fahrenheit
print(f'{c}° Celsius\033[m é igual á \033[1;31m{f}° Fahrenheit.\033[m')
#
# Para cor azul no valor de Celsius: \033[1;34m
# Para cor vermelha no valor de Fahrenheit: \033[1;31m
