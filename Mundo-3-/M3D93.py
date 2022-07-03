"""
Desafio 093

 Solicite o nome do jogador(ou nickname) e quantas partidas ele jogou,
 Solicite também quantas eliminações em cada partida, guarde tudo isso em um
 dicionário, inclua também o total de eliminações feitas pelo jogador durante
 o campeonato, mostre em 3 diferentes formas. """

fncs = {}
partidas = []
print('-='*3, '    FORTNITE BRASIL FNCS    ', '-='*3)
fncs = {"Nome": input('Nome do jogador (ou nick) > ')}
tot = int(input(f'Quantas partidas {fncs["Nome"]} jogou? > '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantas eliminações na {c+1}° partida? > ')))
fncs["Kills"] = partidas[:]
fncs["Total"] = sum(partidas)
print('-='*35)
print(fncs)
print('-='*35)
for keys, values in fncs.items():
    print(f'O campo {keys} tem o valor {values}.')
print('-='*35)
print(f'O jogador {fncs["Nome"]} jogou {partidas} partidas.')
for p, k in enumerate(fncs["Kills"]):
    print(' ' * 5, '=>', f'Na partida {p+1}, fez {[k]} eliminações.', end=' ')
    print()
print(f'Foi um total de {fncs["Total"]} eliminações.')
print('-='*35)
