"""

Desafio 098

Crie uma função chamada contador(), que receba 3 parâmetros: início, fim e
passo e realize 3 contagens, sendo elas: De 1 até 10, de 1 em 1.De 10 até 0,
de 2 em 2.E por fim uma contagem personalizada. """

from time import sleep


def contador(ini, fim, passo):
    print("-="*35)
    sleep(0.5)
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
        sleep(0.5)
        print(c, end='  ', flush=True)
    print("-> FIM")


# Programa principal
contador(1, 10, 1)
contador(10, 0, -2)
print("-="*35)
sleep(1.5)
print("Agora é sua vez de personalizar a contagem!")
print("-="*35)
sleep(0.5)
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)
