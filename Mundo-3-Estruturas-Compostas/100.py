"""

Desafio 100!!!

Crie uma lista chamada números, depois crie 2 funções uma chamada sorteia(), que
vai sortear 5 números aleatórios e coloca-los na lista números, e a outra chamada
somaPar() que vai somar todos os valores pares sorteados pela função anterior."""

from random import randint
from time import sleep

numeros = []


def sorteia():
    print("Sorteando 5 valores para a lista: ", end='')
    for valores in range(0, 5):
        valor = randint(1, 9)
        numeros.append(valor)
        sleep(0.5)
        print(valor, end=' ', flush=True)
    print("PRONTO!")
    sleep(0.5)


def somaPar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de: {numeros}, temos: {soma}")


# Programa principal
sorteia()
somaPar()
