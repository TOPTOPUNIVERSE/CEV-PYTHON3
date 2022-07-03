to = n = t = m = mv = mv2 = 0 
c = 'S'
while c != 'N':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    to += n #Variavel de soma de todos os números inseridos
    t += 1 #Variavel de quantos números foram inseridos
    m = to / t #Variavel de media de todos os números
    if n == 1: #Se número inserido for igual a 1
        mv = mv2= n #Maior valor e menor valor agora são 1
    else: #Caso contrário
        if n > mv: #Se número inserido for maior que o maior número registrado
            mv = n #Maior número agora é o número inserido
        #Se menor valor inserido for igual a 0 ou o número inserido for menor que
        #o menor valor registrado
        if mv2 == 0 or n < mv2: 
            mv2 = n #Menor valor agora é o número inserido
print(f'Você digitou {t} números e a média foi {m:.2f}')
print(f'O maior valor é {mv} e o menor foi {mv2}.')


