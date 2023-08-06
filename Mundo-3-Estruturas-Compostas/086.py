# Crie uma matriz(3x3) e preencha com valores lidos pelo teclado
# no fim mostre a matriz na tela
# Solução mais enxuta guanabara
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
'''minha solução
matriz = [[], [], []]
for c in range(0, 3):
    v = int(input(f'Digite um valor para [0, {c}]: '))
    matriz[0].insert(c, v)
for d in range(0, 3):
    v2 = int(input(f'Digite um valor para [1, {d}]: '))
    matriz[1].insert(d, v2)
for e in range(0, 3):
    v3 = int(input(f'Digite um valor para [2, {e}]: '))
    matriz[2].insert(e, v3)
print('-='*15, 'Matriz 3x3', '-='*15)
for valores in matriz[0]:
    print(f'[ {valores} ]', end=' ')
print()
for valores in matriz[1]:
    print(f'[ {valores} ]', end=' ')
print()
for valores in matriz[2]:
    print(f'[ {valores} ]', end=' ')'''
