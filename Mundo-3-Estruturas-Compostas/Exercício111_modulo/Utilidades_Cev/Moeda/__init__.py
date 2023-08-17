"""

Desafio 111

Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados
moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108, 109 
e 110 para o primeiro pacote e mantenha tudo funcionando."""


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def aumentar(preco=0, taxa=0, formatacao=False):
    res = (preco + (taxa / 100) * preco)
    return res if formatacao is False else moeda(res)


def diminuir(preco=0, taxa=0, formatacao=False):
    res = (preco - (taxa / 100) * preco)
    return res if formatacao is False else moeda(res)


def dobro(preco=0, formatacao=False):
    res = preco * 2
    return res if formatacao is False else moeda(res)


def metade(preco, formatacao=False):
    res = preco / 2
    return res if formatacao is False else moeda(res)


def resumo(preco, aumento, reducao):
    titulo = 'RESUMO DO VALOR'
    tam = len(titulo) + 20
    print('-'*tam)
    print(f'{titulo:^{tam}}')
    print('-'*tam)
    print(f'''Preço analisado: {moeda(preco):>{15}}
Dobro do preço: {dobro(preco, True):>{16}}
Metade do preço: {metade(preco, True):>{15}}
{aumento}% de aumento: {aumentar(preco, aumento, True):>{16}}
{reducao}% de redução: {diminuir(preco, reducao, True):>{16}}''')
    print('-'*tam)

