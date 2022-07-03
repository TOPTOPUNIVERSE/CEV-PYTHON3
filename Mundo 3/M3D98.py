"""

Desafio 098

Crie uma função chamada contador(), que receba 3 parâmetros: início, fim e
passo e realize 3 contagens, sendo elas: De 1 até 10, de 1 em 1.De 10 até 0,
de 2 em 2.E por fim uma contagem personalizada. """

from time import sleep
"""a = int(input("Início: "))
b = int(input("Fim: "))
c = int(input("Passo:"))
print("-="*35)"""
print("-="*35)
print("Contagem de 1 até 10 de 1 em 1.")
for c in range(1, 11):
    print(c, end='  ')
print("-> FIM.")
print("-="*35)
print("Contagem de 10 até 0 de 2 em 2.")
for c in range(10, 0, -2):
    print(c, end='  ')
print("-> FIM.")
print("-="*35)
print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print("-="*35)
if passo > 0:
    print(f"Contagem de {ini} até {fim} de {passo} em {passo}.")
if passo == 0:
    passo = -1
if passo <= -1:
    passo = -passo
    print(f"Contagem de {ini} até {fim} de {passo} em {passo}.")
if fim < ini and passo != 0:
    fim = fim - 1
    if passo > 0:
        passo = -passo
if fim > ini:
    fim = fim + 1
for c in range(ini, fim, passo):
    print(c, end='  ')
print("-> FIM")

# for c in range(20, 10 - 1, 0):
#    print(c, end='  ')
