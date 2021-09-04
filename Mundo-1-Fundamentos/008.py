"""
Desafio 008
Problema: Escreva um programa que leia um valor em metros e o
          exiba convertido em centímetros e milímetros e etc."""

# Solicitando valor em metros
m = float(input('Valor em metros:\033[1;90m '))
# Mostrando na tela o valor em centímetros, milímetros, quilômetros, decimetros
# hectômetros e decâmetros
print(
    f'\033[m\033[1;35mValor em centímetros:\033[m {m * 100:.0f}cm\n \033[1;35mValor em milímetros:\033[m {m * 1000:.0f}mm\n \033[1;35mValor em Quilômetros:\033[m {m/1000}km'
    f'\n \033[1;35mValor em Decimetro:\033[m {m*10:.0f}\n \033[1;35mValor em Hectômetro:\033[m {m/100:.0f}\n \033[1;35mValor em Decâmetros:\033[m {m/10:.0f}')
#
# Para o valor em metros ter a  cor cinza escuro: \033[1;90m
# Para a cor das perguntas ficarem em magenta: \033[1;35m
