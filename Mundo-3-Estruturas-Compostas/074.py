from random import randint #Importando biblioteca para gerar números aleatórios
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
    randint(1, 10), randint(1, 10)) #Tupla com os números aleatórios
print(f'Os números sorteados foram ',end=' ')
for n in numeros: #Para cada número na tupla 'numeros'
    print(f'{n}',end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')