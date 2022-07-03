#Desta forma estamos conectando as listas e não copiando
#teste = list()
#teste.append('Gustavo')
#teste.append(40)
#galera = list()
#galera.append(teste) 
#teste[0] = 'Maria'
#teste[1] = 22
#galera.append(teste)
#print(galera)
#
#Agora sim copiando
#teste = list()
#teste.append('Gustavo')
#teste.append(40)
#galera = list()
#galera.append(teste[:]) # [:]
#teste[0] = 'Maria'
#teste[1] = 22
#galera.append(teste[:])
#print(galera)
#
#
#Exemplo de listas compostas
#galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
#print(galera[3][1])

#Exemplos com for

#galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
#for pessoas in galera:
    #print(pessoas[0],end=',') #Só o nome lado a lado
    #print(pessoas[1]) #Só a idade
    #print(pessoas) #print geral
    #print(f'{pessoas[0]} tem {pessoas[1]} anos de idade.') #Mostrar tudo bonitin

#Exemplo solicitando dados e mostrando apenas maiores de idade
galera = list()
dado = list ()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
 
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Foram cadastrados {totmai} maiores de idade e {totmen} menores de idade.')

#Para criar lista composta
lista = [[], []]