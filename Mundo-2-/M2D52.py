print('-='*10, 'É PRIMO?', '-='*10) #Cabeçalho
n = int(input('Digite um número: ')) #Solicitando número
t = 0 #variavel dos divisiveis
for c in range(1, n + 1): #Laço de validação
    if n % c == 0:
        print(f'\033[1;34m{c}\033[m', end=' ')
        t += 1 #Contador dos divisíveis
    else: 
        print(f'\033[1;31m{c}\033[m', end=' ')
print(f'\nO número {n} foi divisível {t} vezes.') 
if t == 2: #Laço de validação 
    print('E portanto ele é PRIMO !')
else:
    print('E por isso ele NÃO É PRIMO.')
    #cabeçalho