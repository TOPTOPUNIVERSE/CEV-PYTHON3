print('-='*10, 'SOMA DE NUMEROS IMPARES MULTIPLOS DE 3', '-='*10)
s = 0
co = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        co += 1 #co = co + 1
        s += c #s = s + c
print(f'A soma de todos os {co} valores solicitados é {s}')