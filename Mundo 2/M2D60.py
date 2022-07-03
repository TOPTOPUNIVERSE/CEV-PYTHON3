#Da forma mais enxuta
'''from math import factorial
x = int(input('Digite um número: ')) #Solicitando número
f = factorial(x)
print(f'O fatorial de {x} é {f}.')'''
print('>'*10, 'BORA FATORAR?', '<'*10)#Cabeçalho
x = int(input('Digite um número: ')) #Solicitando número
c = x #Variavel do contador
f = 1  #Variavel de fator nulo de multiplicação
print(f'O fatorial de {x} é')
while c > 0: #Enquanto contador for maior do que 0
    print(c, end=' ')
    print('x' if c > 1 else '=',end=' ')
    f *= c #f = f * c
    c -= 1 # c = c - 1
print(f'{f}') #Mostrando o numero inserido fatorado
print('>'*10, 'FIM', '<'*10) #Cabeçalho



