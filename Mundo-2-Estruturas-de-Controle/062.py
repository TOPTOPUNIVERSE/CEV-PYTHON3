print('-='*10, '10  PRIMEIROS TERMOS DA P.A', '-='*10)#Cabeçalho
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t1 = n #Variavel do 1 termo
c = 1 # Variavel do contador
to = 0 #Variavel do total
m = 10 #Variavel dos termos a mais
while m != 0:
    to = to + m 
    while c <= to:
        print(f'{t1} > ',end=' ')
        t1 += r
        c += 1
    print('PAUSA')
    m = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {to} termos mostrados.')
print('-='*10, 'FIM','-='*10) #Cabeçalho0
