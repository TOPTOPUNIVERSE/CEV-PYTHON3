"""
Desafio 095

Solicite o nome de jogadores(ou nickname) e quantas partidas eles jogaram,
Solicite também quantas eliminações em cada partida, guarde tudo isso em um
dicionário, inclua também o total de eliminações feitas por cada jogador durante
o campeonato, no final mostre uma tabela com o número referente aos jogadores, o nome
dos jogadores, as eliminações e o total de eliminações. """

time = []
fncs = {}
partidas = []
print('-='*3, '    FORTNITE BRASIL FNCS    ', '-='*3)
while True:
    fncs.clear()
    partidas.clear()
    fncs = {"Nome": input('Nome do jogador (ou nick) > ')}
    tot = int(input(f'Quantas partidas {fncs["Nome"]} jogou? > '))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantas eliminações na {c+1}° partida? > ')))
    fncs["Kills"] = partidas[:]
    fncs["Total"] = sum(partidas)
    time.append(fncs.copy())
    cont = str(input("Deseja cadastrar mais um jogador?[S/N] > ")).strip().upper()
    while cont not in 'SN':
        print('Dados inválidos! leia com atenção.')
        cont = str(input("Deseja cadastrar mais um jogador?[S/N] > ")).strip().upper()
    if cont in 'N':
        break
print('-='*35)
print(' N° ', end='')
for i in fncs.keys():
    print(f'{i:<15}', end='')
print()
print('-'*65)
for chave, valores in enumerate(time):
    print(f'{chave:>2} ', end='')
    for d in valores.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*35)
while True:
    busca = int(input('Mostrar dados de qual jogador?[999 para parar] > '))
    if busca == 999:
        print('-='*15, 'FIM', '-='*15)
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador {busca}')
    else:
        print(f'--Levantamento do jogador {time[busca]["Nome"]}:')
        for i, k in enumerate(time[busca]["Kills"]):
            print(f'  No jogo {i+1}, fez {k} eliminações.')
    print('-'*65)
