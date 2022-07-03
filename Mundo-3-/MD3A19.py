#Dicionários = {}

# Para exibir um valor da chave

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
# print(pessoas['nome'])

# Para exibir dois valores de chaves individuais

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

# Para mostrar as chaves

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
# print(pessoas.keys())

# Para mostrar os valores

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
# print(pessoas.values())

# Para mostrar os items(ou tudo)

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
# print(pessoas.items())

# Exemplos de for
# For para mostrar as chaves

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
# for k in pessoas.keys():
# print(k)

# Para mostrar os valores

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
# for k in pessoas.values():
# print(k)

# Para mostrar os items

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
# for k, valor in pessoas.items():
#print(f'{k} = {valor}')

# Para Apagar

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
#del pessoas['sexo']
# for k, valor in pessoas.items():
#print(f'{k} = {valor}')

# Para Substitur o valor da chave

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
#pessoas['nome'] = 'Leandro'
# for k, valor in pessoas.items():
#print(f'{k} = {valor}')

# Para adicionar um elemento

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
#pessoas['peso'] = 98.5
# for k, valor in pessoas.items():
#print(f'{k} = {valor}')

# Criando dicionário dentro de uma lista

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil)  # sendo brasil[0] o estado1
#
# print(brasil[1]['sigla']) #Mostra SP
#
# print(brasil[0]['uf'])  # Mostra Rio de janeiro

# Exemplos com solicitação de dados

estado = dict()
brasil = []  # ou list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
# print(brasil)
# Para mostrar mais bonitinho
# for e in brasil:
#    print(e)
# Para mostrar mais bonitinho ainda
# for e in brasil:
    # for k, v in e.items():
    #print(f'O campo {k} tem valor {v}')

# Para mostrar mais bonitinho porém só com o valor
for e in brasil:  # Laço da lista
    for v in e.values():  # Laço do dicionário
        print(v, end=' ')
    print()  # Para pular linha
