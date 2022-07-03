'''
#Solução do guanabara
 r = str(input('Qual o seu sexo?[M/F]: ')).strip().upper()[0]#Solicitando sexo
while r not in 'MF': #Enquanto sexo não for M ou F
    r = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {r.capitalize()} registrado com sucesso !')
print('-='*10, 'FIM','-='*10)'''
#Pra pegar somente a primeira letra [0]
#Minha solção
s = ''
while s != 'M' and s != 'F':
    s = str(input('DIgite o sexo [M/F]: ')).upper().strip()
    if s != 'M' and s != 'F':
        print('Dados inválidos.Por favor digite a letra correta!!!')
if s == 'M':
    s = 'Masculino'
else:
    s = 'Feminino'
print(f'Sexo {s} registrado com sucesso!')