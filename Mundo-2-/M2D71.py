print('='*45) #Cabeçalho
print(' '*15, 'BANCO TOPTOP' ,' '*15)
print('='*45)
v = int(input('Qual valor você deseja sacar? R$')) #Solicita valor
total = v
céd = 50 
totcéd = 0 #Total de determinadas cédulas
while True:
    if total >= céd: #Se total for maior ou igual ao valor da cédula
        total -= céd #Tire  50 reais quantas vezes forem necessárias
        totcéd += 1
    else: #Caso não de pra tirar mais com a cédula de 50 vá para as outras
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*45)




#Minha Solução
'''
cin = vin = de = um = 0 #Variavel de 50,20,10 e 1 recebem 0
while True:
    print('='*45) #Cabeçalho
    print(' '*20, 'BANCO TOPTOP', ' '*20)
    print('='*45)
    v = int(input('Qual valor você deseja sacar? R$')) #Solicita valor
    while v <= 0: #Caso dados inválidos
        v = int(input('Qual valor você deseja sacar? R$')) #Solicitamos valor novamente
    if v == 50:
        cin += 1
        print(f'Total de {cin:.0f} cédulas de R$50')
        break
    if v > 50:
        div = v // 50
        cin += div 
        multi = div * 50
        sub = v - multi
        print(f'Total de {cin:.0f} cédulas de R$50')
        if sub >= 20:
            div = sub // 20
            vin += div
            multi= div * 20
            sub = sub - multi
            print(f'Total de {vin:.0f} cédulas de R$20')
        if sub >= 10:
            div = sub // 10
            de += div
            multi= div * 10
            sub = sub - multi
            print(f'Total de {de:.0f} cédulas de R$10')
        if sub >= 1:
            div = sub // 1
            um += div
            print(f'Total de {um:.0f} cédulas de R$1')
        break
    elif v < 50 and v > 20:
        div = v // 20
        vin += div
        multi = div * 20
        sub = v - multi
        print(f'Total de {vin:.0f} cédulas de R$20')
        if sub >= 10:
            div = sub // 10
            de += div
            multi= div * 10
            sub = sub - multi
            print(f'Total de {de:.0f} cédulas de R$10')
        if sub >= 1:
            div = sub // 1
            um += div
            print(f'Total de {um:.0f} cédulas de R$1')
        break
    elif v == 20:
        vin += 1
        print(f'Total de {vin:.0f} cédulas de R$20')
        break
    elif v < 20 and v > 10:
        div = v // 10
        de += div
        multi = div * 10
        sub = v - multi
        print(f'Total de {de:.0f} cédulas de R$10')
        if sub >= 1:
            div = sub // 1
            um += div
            print(f'Total de {um:.0f} cédulas de R$1')
        break
    elif v == 10:
        de += 1
        print(f'Total de {de:.0f} cédulas de R$10')
        break
    elif v < 10: 
        div = v // 1
        um += div
        print(f'Total de {um:.0f} cédulas de R$1')
        break
    elif v == 1:
        print(f'Total de {um:.0f} cédulas de R$1')
        um += 1
        break
    print('='*45)'''