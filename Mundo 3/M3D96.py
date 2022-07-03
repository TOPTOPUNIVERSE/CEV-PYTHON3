"""

Desafio 096

Crie uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno. """


def area(largura, comprimento):
    total = largura * comprimento
    print(f"A área de seu terreno de {largura}x{comprimento} é de {total}m².")


# Programa principal
print("  Controle de Terrenos  ")
print("-"*30)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)
