"""

Desafio 099

Crie uma função chamada maior() que receba vários parâmetros com valores inteiros,
seu programa deverá analisar todos os valores e dizer qual deles é o maior, também
deverá informar quantos valores foram informados."""

from time import sleep


def maior(* núm):
    print("Analisando os valores passados...")
    if len(núm) != 0:
        for valor in núm:
            sleep(0.3)
            print(valor, end=' ', flush=True)
        sleep(0.5)
        print(f"Foram informados {len(núm)} valores ao todo.")
        sleep(0.5)
        print(f"O maior valor informado foi {max(núm)}.")
        print("-="*35)
    elif len(núm) == 0:
        sleep(0.5)
        print(f"Foram informados {len(núm)} valores ao todo.")
        sleep(0.5)
        print(f"O maior valor informado foi 0.")


# Programa principal
print('-='*35)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
