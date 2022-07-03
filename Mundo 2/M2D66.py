print('~'*10, 'Bora somar?', '~'*10) #Cabeçalho
s = c = 0 #Variaveis de soma e contador recebem 0
while True: #Enquanto verdade
    n = int(input('Digite um número [ou 999 para parar]: ')) #Solicitando número
    if n == 999: #Se o número solicitado for igual a 999
        break #Pare
    s += n #Somando os números digitados
    c += 1 #Contabilizando quantos números foram digitados
print(f'Foram digitados {c} números e a soma entre eles é {s}!.')
print('~'*10, 'FIM', '~'*10) #Cabeçalho de fim