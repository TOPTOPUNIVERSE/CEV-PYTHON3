# Crie uma matriz(3x3) e preencha com valores lidos pelo teclado
# no fim mostre a matriz na tela, a soma dos pares, a soma da 3 coluna
# e o maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da 3° coluna é {scol}')
for coluna in range(0, 3):
    if coluna == 0:
        mai = matriz[1][coluna]
    elif matriz[1][coluna] > mai:
        mai = matriz[1][coluna]
print(f'O maior valor da segunda linha é {mai}')

'''minha  1 solução
matriz = [[], [], [], []]
somapar = soma_col = 0
for c in range(0, 3):
    v = int(input(f'Digite um valor para [0, {c}]: '))
    matriz[0].insert(c, v)
    if len(matriz[0]) == 3:
        soma_col += matriz[0][2]
    if v % 2 == 0:
        matriz[3].append(v)
        somapar += v
for d in range(0, 3):
    v2 = int(input(f'Digite um valor para [1, {d}]: '))
    matriz[1].insert(d, v2)
    if len(matriz[1]) == 3:
        soma_col += matriz[1][2]
    if v2 % 2 == 0:
        matriz[3].append(v2)
        somapar += v2
for e in range(0, 3):
    v3 = int(input(f'Digite um valor para [2, {e}]: '))
    matriz[2].insert(e, v3)
    if len(matriz[2]) == 3:
        soma_col += matriz[2][2]
    if v3 % 2 == 0:
        matriz[3].append(v3)
        somapar += v3
print('-='*15, 'Matriz 3x3', '-='*15)
for valores in matriz[0]:
    print(f'[ {valores} ]', end=' ')
print()
for valores in matriz[1]:
    print(f'[ {valores} ]', end=' ')
print()
for valores in matriz[2]:
    print(f'[ {valores} ]', end=' ')
print()
print(f'-='*35)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da 3° coluna é  {soma_col}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')'''
