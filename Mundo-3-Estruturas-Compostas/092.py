# Solicite nome, ano de nascimento, carteira de trabalho(ctps),ano de contratação
#  e salário, pegue esses dados e coloque em um dicionário pegue também o ano de
# nascimento e descubra a idade do usuário, mostre no final todos os dados na tela +
# Quantos anos a pessoa vai se aposentar, sendo em conta 35 anos de contribuição.

from datetime import date

ano_atual = date.today().year
print('-='*35)
pessoas = {"Nome": str(input('Nome: ')).strip().capitalize(),
           "Idade": ano_atual - int(input('Ano de nascimento: ')),
           "Ctps": int(input('Carteira de Trabalho (0 não tem): '))}
if pessoas["Ctps"] != 0:
    pessoas["Contratação"] = int(input('Ano de contratação: '))
    pessoas["Salário"] = int(input('Salário: '))
    pessoas["Aposentadoria"] = pessoas["Idade"] + ((pessoas["Contratação"] + 35) - ano_atual)
print('-='*35)
for keys, values in pessoas.items():
    print(f'{keys} tem o valor {values}')
