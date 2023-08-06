"""

Desafio 097

Crie uma função chamada escreva() que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável. """


def escreva(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"{msg:^{tam}}")
    print("~"*tam)


# Programa principal
msg = str(input("Informe uma mensagem: ")).strip().capitalize()
escreva(msg)
