# Solicite nome e média de um aluno e guarde tudo isso + a situação do aluno
# em um dicionário onde se a média for >= a 7 ele foi aprovado
# caso contrário reprovado

dados = {}

dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Média'] >= 7:
    dados['Situação'] = "aprovado!! :)"
elif dados['Média'] >= 5 and dados['Média'] < 7:
    dados['Situação'] = "recuperação :("
else:
    dados['Situação'] = "reprovado! :("
print('-='*35)
for k, d in dados.items():
    print(f' - {k} é igual a {d}')
