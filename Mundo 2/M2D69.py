dm = h = m = 0 #Variaveis de maioridade, homem e variavel mulher recebem 0
while True:
    print('-='*35) #Cabeçalho 
    print('CADASTRE UMA PESSOA')
    print('-='*35)
    i = int(input('Digite sua idade: ')) #Solicitando idade
    s = str(input('Digite o seu sexo [M/F]: ')).strip().upper() #Solicitando seqsu
    while s not in 'M' and s not in 'F': #Caso dados inseridos sejam inválidos
        s = str(input('Digite o seu sexo [M/F]: ')).strip().upper()#Solicite novamente
    c = str(input('Deseja continuar? [S/N]: ')).strip().upper() #Variavel de continuação
    if i > 18:
        dm += 1 #Contabilizando maior de 18
    if s == 'M':
        h += 1 #Contabilizando um homem cadastrado
    elif s == 'F' and i < 20:
        m += 1 #Contabilizando uma mulher com menos de 20 anos cadastrada
    while c not in 'N' and c not in 'S': #Caso dados inválidos
        c = str(input('Deseja continuar? [S/N]: ')).strip().upper() #Solicite novamente
    if c == 'N':
        break #Pare o programa se o usuário não desejar continuar
print('-'*55) #Cabeçalho
print(f'Ao todo {dm} pessoas tem mais de 18 anos.') #Mostre as estatísticas
print(f'{h} homens foram cadastrados\nE {m} mulheres com menos de 20 anos foram cadastradas.') 
print('-='*15, 'FIM', '-='*15)
