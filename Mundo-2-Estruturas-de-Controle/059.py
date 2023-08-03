print('-='*10, 'Quase uma calculadora...','-='*10)#Cabeçalho
v = int(input('Digite um valor: ')) #Solicitando valor
v2 = int(input('Digite outro valor: ')) #Solicitando valor
c = 0 #Variavel de opção
while c != 5: #Enquanto opção for diferente de 5
    #Mostrando o menu
    print('''    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos números
    [ 5 ] - Sair''')
    c = int(input('>>>>>>>>>>> Informe sua opção: ')) #Solicitando opção
    if c == 1: #Se opção 1 for escolhida
        print(f'Os números {v} e {v2} somados são {v + v2} ')
    elif c == 2: #Se opção 2 for escolhida
        print(f'Os números {v} e {v2} multiplicados são {v * v2}')
    elif c == 3: #Se opção 3 for escolhida
        if v > v2:
            m = v
        elif v == v2:
            print(f'Ambos os valores {v} e {v2} são iguais.')
        elif v2 > v:
            m = v2
        print(f'Entre os números {v} e {v2} o maior número é {m}')
    elif c == 4: #Se opção 4 for escolhida
        print('Informe os números novamente')
        v = int(input('Digite um valor: ')) #Solicitando valor
        v2 = int(input('Digite outro valor: ')) #Solicitando valor
print('-='*10, 'FIM', '-='*10)