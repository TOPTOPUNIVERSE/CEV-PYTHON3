from datetime import date #Importando biblioteca de data
print('-='*10, 'É DE MAIOR?', '-='*10) #Cabeçalho
a = date.today().year #Variavel do ano atual
tm = 0 #Variavel de maiores
tn = 0 #Variavel de menores
for p in range(0,7):
    n = int(input('Digite sua data de nascimento: ')) #Solicitando data de nascimento
    i = a - n #Variavel de idade
    if i >= 18:
        print(f'Sua idade é {i}\nLogo é de MAIOR.')
        tm +=1
    else:
        print(f'Sua idade é {i}\nPortanto é de menor.')
        tn += 1
print(f'Ao todo tivemos {tm} pessoas maiores de 18 anos, e {tn} menores.')
print('-='*10, 'FIM', '-='*10) #Cabeçalho
