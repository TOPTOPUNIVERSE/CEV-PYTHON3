# leia nome e duas notas e vários alunos, guarde em uma única lista composta
# Mostre o boletim com a média de cada um de escolha ao usuário para ver as
# notas de cada aluno individualmente

bo = []
while True:
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    n1 = float(input('Digite sua média do provão: '))
    n2 = float(input('Digite sua nota da redação: '))
    media = (n1 + n2) / 2
    bo.append([nome, [n1, n2], media])
    cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    while cont not in 'SN':
        print('Dados Inválidos!')
        cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if cont in 'N':
        break
print('-='*35)
print(f'{"N°":<4}{"NOME":<10} {"MÉDIA":>8}')
for indice, aluno in enumerate(bo):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('-='*35)
while True:
    m = int(input('Mostrar notas de qual aluno? [999 para parar]: '))
    if m <= len(bo) - 1:
        print(f'Notas de {bo[m][0]} são {bo[m][1]}')
        print('-'*35)
    if m == 999:
        print('-='*15, 'FIM', '-='*15)
        break
