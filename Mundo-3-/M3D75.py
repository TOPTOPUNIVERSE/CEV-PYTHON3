#Solicitando 4 valores para coloca-los em uma tupla
#Quantas vezes apareceu o nove? e em que posição apareceu o 3?
#Quais valores são pares?
tupla = (int(input('Digite um número: ')), #Solicitando valores 
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valores: {tupla}')
if 9 in tupla: #Verificando existencia do 9 na tupla
    print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
else:
    print('O valor 9 não apareceu nenhuma vez.')
if 3 in tupla: #Verificando existencia do 3 na tupla
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print(f'Os valores pares digitados foram: ',end='')
for valor in tupla:
    if valor % 2 == 0: #Checando quais valores são pares
        print(valor,end=' ')
    else:
        print('Nenhum')
        break

