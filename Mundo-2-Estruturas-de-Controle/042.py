#Cabeçalho do programa
print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))#Solicitando o segmento 1
r2 = float(input('Segundo segmento: '))#Solicitando o segmento 2
r3 = float(input('Terceiro segmento: '))#Solicitando o segmento 3
#Validação para ver se é possível montar um triângulo com os segmentos
if r1 <= r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    #Mostrando na tela que podem formar um triângulo
    print(f'Os segmentos PODEM formar um triângulo', end=' ')
    #Se todos os lados são iguais
    if r1 == r2 == r3:
        #Mostre que é equilátero
        print('EQUILÁTERO!')
    #elif r1 == r2 or r2 == r3 or r3 == r1: (outra forma de fazer!!)
        #print('ISÓSCELES!')'''
    #Se todos os lados são diferentes
    elif r1 != r2 != r3 != r1:
        #Mostre na tela que é escaleno
        print('ESCALENO!')
        #Caso contrário  
    else:
        #Mostre na tela que é isósceles
        print('ISÓSCELES!')
#Caso contrário
else:
    #Mostre que não podem formar um triângulo
    print('Os segmentos NÃO podem formar um triângulo.')
#Cabeçalho do fim de programa
print('-=-'*20)
print('END')
print('-=-'*20)
#
