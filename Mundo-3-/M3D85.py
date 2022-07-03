# Leia 7 valores coloque todos os valores em uma unica lista(composta) que seja composta
# por 2 listas(2 listas dentro de 1 lista) uma de pares e outra de impares
# Mostre os pares e impares em ordem crescente
valores = [[], []]  # Lista composta
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    if valor % 2 != 0:
        valores[1].append(valor)
print('-='*35)
print(f'Os valores pares são {sorted(valores[0])}\nOs valores impares são {sorted(valores[1])}')
