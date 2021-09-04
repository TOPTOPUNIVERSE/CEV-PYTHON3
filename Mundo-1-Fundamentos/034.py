"""
Desafio 034
Problema: Escreva um programa que pergunte o salário de um funcionário
          e calcule o valor do seu aumento. Para salários superiores a
          R$1250,00, calcule um aumento de 10%. Para os inferiores ou
          iguais, o aumento é de 15%."""

so = float(input('Qual o seu salário atual? R$'))  # Pedindo o salário atual
sn = so + (so * 15) / 100  # Calculando o salário com 15% de aumento
sa = so + (so * 10) / 100  # Calculando o salário com 10% de aumento
if so <= 1250:  # Se o salário for até um salário minímo,o aumento é de 15%
    print(f'Seu novo salário é: R${sn:.2f} com 15% de aumento parabéns ! ! !')
else:  # Se o salário é mais do que um salário minímoo aumento é de  10%
    print(f'Seu novo salário é: R${sa:.2f} com 10% de aumento parabéns ! ! !')
