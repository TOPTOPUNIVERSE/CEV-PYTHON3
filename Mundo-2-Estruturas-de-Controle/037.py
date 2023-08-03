#Cabeçalho do Programa
print('-=-'*10, 'Conversor de Bases númericas', '-=-'*10)
#Solicitando número inteiro
n = int(input('Digite um número inteiro qualquer: '))
    #Mostrando na tela as opções
print(''' Escolha uma das bases para conversão:
    [ 1 ] Binário
    [ 2 ] Octal
    [ 3 ] Hexadecimal
    [ 4 ] Sair''')
    #Solicitando escolha das opções
op = int(input('Escolha sua opção: '))
#Se opção 1 for escolhida
if op == 1:
    #Mostre na tela o programa da função 1
    print(f'{n} Em base binária é igual á {n:b}')
#Se opção 2 for escolhida
elif op == 2:
    #Mostre na tela o programa da função 2
    print(f'{n} Em base octal é igual á {n:o}')
#Se opção 3 for escolhida
elif op == 3:
    #Mostre na tela o programa da  função 3
    print(f'{n} Em base hexadecimal é igual á {n:x}')
else:
    print('Opção Inválida!, tente novamente.')
#Cabeçalho de finalização
print('-=-' * 10, 'Programa encerrado', '-=-' * 10)
