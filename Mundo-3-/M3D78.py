#Leia 5 valores númericos adicioneos em uma lista e no final
#mostre o maior e o menor valor e suas respectivas posições
valores = [] #Lista
maior = menor = 0
for valor in range(0, 5): #Solicitando os valores
    valores.append(int(input(f'Digite um valor para a posição {valor}: ')))
    if valor == 0:
        maior = menor = valores[valor]
    else:
        if valores[valor] > maior:#Checando quem é o maior e quem é o menor
            maior = valores[valor]
        if valores[valor] < menor:
            menor = valores[valor]
print('-'*45)
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for pos,valor in enumerate(valores):#Checando as posições dos maiores valores
    if valor == maior:
     print(f'{pos} >>> ',end='')
print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for pos,valor in enumerate(valores): #Checando a posição dos menores valores
    if valor == menor:
        print(f'{pos} >>> ',end='')
print(f'\nVocê digitou os valores {valores}')
print('-'*45)