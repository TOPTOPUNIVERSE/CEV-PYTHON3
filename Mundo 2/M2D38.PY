#Cabeçalho de identificação do programa
print('=-=' *10 , 'Qual valor é maior?', '=-=' *10)
#Solicitand número inteiro
n1 = int(input('Digite um número inteiro: '))
#Solicitando  outro número inteiro
n2 = int(input('Digite outro número inteiro: '))
#Se o primeiro valor for maior que o segundo valor digitado
if n1 > n2:
    #Mostre na tela que o primeiro valor é o maior
    print('O primeiro valor é maior.')
    #Se o segundo valor for maior que o primeiro valor digitado
elif n2 > n1:
    #Mostre que o segundo valor é o maior
    print('O segundo valor é maior.')
#Caso os valores sejam iguais
else:
    #Mostre na tela que não á valor maior
    print('Não existe valor maior, os dois são iguais.')
#Cabeçalho de fim do programa
print('=-='*10, 'END', '-=-' *10)
#