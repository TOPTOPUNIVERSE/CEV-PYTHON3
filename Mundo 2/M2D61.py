print('-='*10, '10  PRIMEIROS TERMOS DA P.A', '-='*10)#Cabeçalho
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t1 = n #Variavel do 1 termo
c = 1 # Variavel do contador
'''d = n + (10 - 1) * r 
print(f'Os 10 primeiros termos da P.A que inicia com {n} e tem razão {r}'
    f'\nsão')
for c in range (n, d + r, r):
    print(c,end=' > ')
print('Fim')'''
while c <= 10:
    print(f'{t1} > ',end=' ')
    t1 += r
    c += 1
print('FIM')
print('-='*10, 'FIM','-='*10) #Cabeçalho0
