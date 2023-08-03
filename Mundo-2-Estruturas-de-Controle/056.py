ti = 0 #Variavel de total de idades
e = 0 #Variavel de 'elder' mais velho
nv = '' #Variavel de nome do mais velho
l = 0 #Variavel de 'less' menor de 20 anos
for c in range(1, 5): 
    print('-='*10, f'{c}° Pessoa', '-='*10) 
    n = str(input('Digite seu nome: ')).strip().capitalize() #Solicitando nome
    a = int(input('Digite sua idade: ')) #Solicitando idade
    s = str(input('Digite seu sexo [M/F]: ')).strip().upper() #Solicitando sexo
    ti += a #Somando as idades
    m = ti / 4 #Dividindo as idades por 4 para obter a média
    #Se variavel 's' for = M e variavel 'e' for menor que 'a'
    if s in 'M' and e < a: 
        e = a #Variavel 'e' recebe 'a'
        nv = n #Variavel 'nv' recebe 'n'
    elif a < 20 and s == 'F': #Se 'a' for menor que 20 e 's' for igual a F
        l += 1 #Variavel 'l' adiciona 1 em sua contagem
print(f'A média de idade do grupo é {m} anos.')
print(f'O homem mais velho tem {e} anos e se chama {nv}.')
print(f'Ao todo são {l} mulheres com menos de 20 anos.')