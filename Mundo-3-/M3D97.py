"""

Desafio 097

Crie uma função chamada escreva() que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável. """


def escreva(msg):
    if len(msg) > 20:
        print("~~"*15)
        print(f"{msg:>27}")
        print("~~"*15)
    elif len(msg) > 10:
        print("~~"*10)
        print(f"{msg:>18}")
        print("~~"*10)
    elif len(msg) < 5:
        print("~~"*3)
        print(f"{msg:>4}")
        print("~~"*3)


titulo = "Gustavo Guanabara"
escreva(titulo)
#
#
titulo1 = "CeV"
escreva(titulo1)
#
titulo2 = "Curso de Python no YouTube"
escreva(titulo2)
#
