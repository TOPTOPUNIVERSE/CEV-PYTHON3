#Cabeçalho do programa
print('=_='*10, 'Calculo de desconto', '=_='*10)
#Solicitando o preço do produto
p = float(input('Diz ai quanto tá: R$'))
#Variavel para receber a opção do usuário
op = -1
#Enquanto opção for diferente de 5
while op != 5:
    #Mostrando as opções de pagamento
    print('1 - Á vistam em dinheiro ou cheque, ganha 10% de desconto.')
    print('2 - Á vista no cartão, ganha 5% de desconto.')
    print('3 - Em até 2 vezes no cartão, SEM JUROS !')
    print('4 - Em 3x ou mais no cartão, com 20% de juros')
    print('5 - Sair ')
    #Solicitando escolha
    op = int(input('Escolha a forma de pagamento: '))
    #Se opção escolhida for igual a 1
    if op == 1:
        #Calculando a porcentagem
        d = (p / 100) * 10
        #Calculando o desconto
        vf = p - d
        #Mostre o valor final da opção correspondente
        print(f'O valor final é R${vf:.2f}')
        #Pare o laço
        break
    #Se opção escolhida for igual a 2
    elif op == 2:
        #Calculando a porcentagem
        d = (p / 100) * 5
        #Calculando o desconto
        vf = p - d
        #Mostre o valor final da opção correspondente
        print(f'O valor final é R${vf:.2f}')
        #Pare o laço
        break
    #Se opção escolhida for igual a 3
    elif op == 3:
        #Mostre o valor final da opção correspondente
        pa = p / 2
        #Mostrando a quantidade de parcelas
        print(f'Sua compra será parcelada em 2x de R${pa:.2f}')
        #Mostrando o valor final
        print(f'O valor final é R${p:.2f}')
        #Pare o laço
        break
    #Se opção escolhida for igual a 4
    elif op == 4:
        #Calculando a porcentagem
        j = (p / 100) * 20
        #Calculando o juros
        vf = p + j
        #Solicitando parcela
        tpa = int(input('Quantas parcelas? '))
        #Calculo da parcela
        pa = vf / tpa 
        #Mostrando o valor das parcelas
        print(f'Sua compra será parcelada em {tpa}x de R${pa:.2f} com juros !')
        #Mostre o valor final da opção correspondente
        print(f'O valor final é R${vf:.2f}')
        #Pare o laço
        break
    #Caso usuário digite opção inexistente
    else:
        #Mostre opção inválida
        print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
        break
#Cabeçalho de fim do programa
print('=_=', 'END', '=_=')
