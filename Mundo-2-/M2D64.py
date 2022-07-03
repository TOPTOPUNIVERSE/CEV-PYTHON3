n = to = t = 0 #Todas as variaveis recebem 0
n = int(input('Digite um número[ou 999 para parar]: ')) #Solicitando número
while n != 999: #Enquanto número solicitado for diferente de 0
    to += n #Guarde e some cada número inserido
    t += 1 #Contabilize quantos números foram digitados
    n = int(input('Digite um número[ou 999 para parar]: ')) #Solicite número
print(f'Foram digitados {t} números e a soma entre eles é {to}') 
