print('>'*10, 'SOMA DOS PARES', '<'*10)#Cabeçalho
s = 0
co = 0 
ni = int(input('Mostre a soma dos pares do número: '))
nf = int(input('ao número: '))
for c in range (ni, nf):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        s += n #s = s + n
        co += 1 #co = co + 1
print (f'Você informou {co}° números PARES e a soma foi {s}.')
print('>'*10,'FIM', '<' *10) #Cabeçalho