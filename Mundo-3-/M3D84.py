#Cadastre pessoas e seu peso e mostre os mais pesados,isto é aqueles que estão 
#entre 100 kg ou mais, mostre também os mais leves(aqueles que estão entre 70kg
# ou menos) e mostre quantas pessoas foram cadastradas

lista = []
dados = []
maior = menor = 0
while True: 
    dados.append(str(input('Nome: '))) 
    dados.append(float(input('Peso: ')))
    if len(lista) == 0: #Se for a primeira vez
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    cont = str(input('Deseja continukar ? [S/N]: ')).upper().strip()
    while cont not in 'SN':
        print('Dados Inválidos! tente novamente')
        cont = str(input('Deseja continuar ? [S/N]: ')).upper().strip()
    if cont in 'N':
        break
print('-='*35)
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi {maior}Kg.Peso de ',end=' ')
for pessoas in lista:
    if pessoas[1] == maior:
        print(f'[{pessoas[0]}] ',end=' ')
print()
print(f'O menor peso foi {menor}Kg.Peso de ',end=' ')
for pessoas in lista:
    if pessoas[1] == menor:
        print(f'[{pessoas[0]}] ', end=' ')
print()


        
    