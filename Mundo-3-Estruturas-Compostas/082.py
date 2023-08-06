print('-='*10, 'Checagem de Pares e Ímpares','-='*10) #Cabeçalho
lista = []
while True:
    lista.append(int(input('Digite um valor: '))) #Solicitando valor
    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while cont not in 'SN': #Caso dados inválidos
        cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if cont in 'N':
        break
pares = []
impares = []
for valor in lista:
    if valor % 2 == 0: #Se for par
        pares.append(valor)
    if valor % 2 != 0: #Se não for
        impares.append(valor)
print('-'*45)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}\nA lista de ímpares é: {impares}')
print('-='*35)
