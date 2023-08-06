"""

Desafio 104

Crie uma função chamada leiaint(),que vai funcionar de forma semelhante á função
input() do Python, só que fazendo a validação para aceitar apenas um valor númerico."""


def leiaint(text):
    n = str(input(text)).strip()
    if n.isnumeric() == True:
        return n
    while n.isnumeric() == False:
        print("\033[1;31m\nERRO! Digite um número inteiro válido.\033[m")
        n = str(input(text)).strip()
    return n


# Programa principal
n = leiaint('Digite um número: ')
print(f"Você acabou de digitar o número {n}.")
