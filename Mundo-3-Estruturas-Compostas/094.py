"""
Desafio 094

Solicite nome, sexo e idade de várias pessoas, guarde os dados de cada pessoa 
em um dicionário,e os dicionários em uma lista, no final mostre quantas pessoas
foram cadastradas, a média do grupo, uma lista com todas as mulheres e uma lista
com todas as pessoas com idade acima da media. """

dados = {}
pessoas = []
soma_idades = media = 0
while True:
    dados.clear()
    dados["Nome"] = str(input('Nome: ')).strip().capitalize()
    dados["Sexo"] = str(input('Sexo[M/F]: ')).strip().upper()
    while dados["Sexo"] not in 'MF':
        print('Dados inválidos! leia com atenção.')
        dados["Sexo"] = str(input('Sexo[M/F]: ')).strip().upper()
    dados["Idade"] = int(input('Idade: '))
    if dados["Idade"] != 0:
        soma_idades += dados["Idade"]
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while cont not in 'SN':
        print('Dados inválidos! leia com atenção.')
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    pessoas.append(dados.copy())
    if cont in 'N':
        break
media = soma_idades / len(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é  de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for valores in pessoas:
    if valores['Sexo'] in "F":
        print(f'{valores["Nome"]} ;', end=' ')
print(f'\n- Lista das pessoas que estão acima da média: ')
print()
for v in pessoas:
    if v["Idade"] > media:
        for keys, values in v.items():
            print(f'{keys} = {values}; ', end=' ')
        print()
print('-='*15, 'FIM', '-='*15)
