#Solicita o valor da casa
vo = float(input('Informe o valor da casa: R$ '))
#Solicitando o sálario do comprador
so = float(input('Informe o seu salário: R$'))
#Solicitando tempo de pagamento
to = float(input('Informe em quantos anos planeja pagar: R$ '))
#
#Transformando o valor anual em mensal
tf = to * 12
#Dividindo o salário pelo valor mensal
pm = vo / tf
#Mostrando na tela o valor da prestação mensal
print(f'Sua prestação mensal será no valor de: {pm:.2f}')
#Variavel para checar se a prestação não excede 30% do salário
v = ( so / 10 ) * 3
#Se execede os 30%
if pm >= v:
    #Mostre na tela empréstimo negado
    print('Valor de prestação excede 30% do salário', end='')
    print(' logo não será possível o financiamento.')
#Se não excede 
else:
    #Mostre na tela empréstimo aceito
    print('Empréstimo aceito ! Você está apto a financiar este imóvel.')
#
