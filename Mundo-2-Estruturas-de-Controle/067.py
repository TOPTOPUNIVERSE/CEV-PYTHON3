print('-='*10, 'TABUADA', '-='*10) #Cabeçalho
while True: 
    print('-'*45)
    n = int(input('Deseja ver a tabuada de qual valor? ')) #Solicitando valor
    print('-'*45)
    if n <= 0: #Se o número solicitado for menor ou igual a 0
        print('Dados Inválidos.') #Mostre dados inválidos
        break #Interrompa o programa
    for c in range(1, 11): 
        print(f'{n} x {c}: {n * c}') #Mostre a tabuada do número solicitado
print('-'*45)
print('-='*10, 'FIM','-='*10)
