#Solicite 5 números, adicione-os em uma lista e mostre em ordem
#sem usar o sorted
print('-='*10,'Colocando em ordem crescente 5 valores','-='*10) #
lista = []
for valor in range(0, 5):
    v = int(input('Digite um valor: ')) #Solicite o valor
    if valor == 0 or v > lista[-1]:
        lista.append(v)
        #print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                #print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-'*75)
print(f'Os valores digitados em ordem foram {lista}')
print('-='*40)