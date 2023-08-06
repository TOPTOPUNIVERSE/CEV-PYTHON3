"""

Desafio 103

Crie uma função chamada ficha(), que receba dois parâmetros opcionais, o 1°
chamado nome, receberá o nome do jogador. E o 2° receberá quantas Kills ele
fez. No fim mostre a ficha do jogador mesmo que algum dado não tenha sido
informado corretamente."""


def ficha(nome='<desconhecido>', kills=0):
    if nome == '':
        nome = '<desconhecido>'
    if kills.isnumeric():
        kills = int(kills)
    else:
        kills = 0
    return f"O jogador {nome} fez {kills} eliminações no campeonato."


nome = str(input("Nome do Jogador: ")).strip().capitalize()
kills = str(input("Número de Kills: "))
print(ficha(nome, kills))
