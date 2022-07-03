#Adicionando valores em uma lista infinita
#mostrando quantos valores foram adicionados e
#depois mostrando os valores em ordem decrescente e
#checando existencia do 5 na lista
valores = [] #Lista com os valores
print('>'*45)
while True:
    valores.append(int(input('Digite um valor: '))) #Solicitando valores
    cont = str(input('Deseja continuar? [S/N]:')).upper().strip()
    while cont not in 'SN': #Caso dados inválidos
        cont = str(input('Deseja continuar? [S/N]:')).upper().strip()
    if cont in 'N':
        break
print('-'*45)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True) #Mostrando a lista em ordem decrescente
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores: #Checando existência do 5 na lista
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado.')
print('>'*25, 'FIM','<'*25)