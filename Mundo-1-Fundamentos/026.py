"""
Desafio 026
Problema: Faça um programa que leia uma frase pelo teclado
          e mostre quantas vezes aparece a letra "A", em que
          posição ela aparece a primeira vez e em que posição
          ela aparece a última vez."""
# Solicitando uma frase
f = str(
    input('Digite uma frase:')).strip().lower().replace(
    "ã", "a").replace(
    "á", "a").replace(
    "à", "a").replace(
    "â", "a")
# Mostrando na tela quantas letras 'A' apareceram
# E a primeira e a última posição em que apareceram
print(f'A letra A aparece \033[1;31m{f.count("a")}\033[m vezes na mesma frase... \n'
      f'A primeira letra \033[1;31mA\033[m apareceu na posição \033[1;34m{f.find("a")+1}\033[m\n'
      f'A última letra \033[1;31mA\033[m apareceu na posição \033[1;93m{f.rfind("a")+1}\033[m')
#
# Para a cor vermelha na quantidade de 'A' que ocorrem na frase: \033[1;31m
# Para a cor azul da primeira posição em que o 'A' ocorre: \033[1;34m
# Para a cor amarela da última posição em que o 'A' ocorre: \033[1;93m
