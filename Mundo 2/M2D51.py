print('-='*10, '10  PRIMEIROS TERMOS DA P.A', '-='*10)#Cabeçalho
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = n + (10 - 1) * r 
print(f'Os 10 primeiros termos da P.A que inicia com {n} e tem razão {r}'
    f'\nsão')
for c in range (n, d + r, r):
    print(c,end=' > ')
print('Fim')

    
    
    