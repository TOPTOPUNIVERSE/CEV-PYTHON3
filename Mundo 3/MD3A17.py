#lista = [2, 5, 9, 1]
#Tanto faz criarmos a lista assim
#valores = []
#ou assim
#valores = list()
#Para inserir 

#lista.insert(2, 0) #Para inserir na posição 2 o valor 0 
#print(lista)
#lista [2] = 3 #Para substituir o valor da posição 2 por 3
#lista.append(7)#Para adicionar valor no fim da lista

#Para mostrar em ordem

#lista.sort()
#lista.sort(reverse=True)#Para mostrar em ordem contrária
#print(lista)

#Para remover o último elemento da lista

#lista.pop() #Remove o último elemento da lista
#lista.pop(2) #Remove o elemento da posição 2

#Para checar se determinado elemento existe na lista e então remove-lo
#if 4 in lista:
    #lista.remove(4)
#else: 
    #print('Não achei o número 4')

#Para saber quantos elementos tem na lista

#print(f'Essa lista tem {len(lista)} elementos!')

#Para mostrar bonitinho colchetes

#valores = []
#valores.append(5)
#valores.append(6)
#valores.append(7)

#for valor in valores:
    #print(f'{valor} > ', end='')

#Para mostrar as chaves 

#valores = []
#valores.append(5)
#valores.append(6)
#valores.append(7)

#for chave,valor in enumerate(valores): #Enumerate pega tanto a chave quanto o valor
    #print(f'Na posição {chave} encontrei o valor {valor}')
#print('Cheguei ao final da lista!')

#Para ler valores pelo teclado e colocar dentro da lista

#valores = []

#for cont in range(0 ,5):
    #valores.append(int(input('Digite um valor: ')))

#for chave,valor in enumerate(valores):
    #print(f'Na posição {chave} encontrei o valor {valor}')
#print('Cheguei ao final da lista!')

#É possível conectar uma lista a outra

#a = [2, 3, 4, 7]
#b = a
#b[2] = 8
#print(f'Lista A: {a}')
#print(f'Lista B: {b}')

#Copiando uma lista

a = [2, 3, 4, 7]
b = a[:] #Todos os valores de a vão para b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
