#Cabeçalho do programa
print('-=-'*10, 'Calculo de alistamento do exército', '-=-'*6)
#Importando bilioteca para data atual
from datetime import date
#Criando variavel para data atual
d = date.today().year
#Mostrando na tela o ano atual
#print(d.year)
print(''' Bem-vindo, Escolha uma opção:
      [ 1 ] Sou Homem
      [ 2 ] Sou mulher ''')
#Solicitando o sexo
s = int(input('Informe o seu sexo: '))
if s == 2:
    print('Você é mulher logo não é obrigatório o alistamento militar.')
elif s == 1:
    #Solicitando o ano de nascimento
    n = int(input('Informe o ano de nascimento: '))
    #Calculando a idade
    i = d - n
    #Mostrando na tela a idade
    print(f'Sua idade é {i}')   
    #Se a idade for menor que 18 anos
    if i < 18:
        #Mostre na tela que não chegou a hora
        print('Calma mlk ainda não chegou a hora...')
        #Variavel para saber quantos anos falta para os 18
        f = 18 - i
        #Se faltar apenas 1 ano para os 18 
        if f == 1:
            #Mostre na tela que falta apenas 1 ano
            print(f'Ainda falta {f} ano para você se alistar.')
        #Se faltar mais que 1 ano para os 18
        elif f > 1:
            #Mostre na tela quantos anoS faltam para os 18
            print(f'Ainda faltam {f} anos para você se alistar.')
    #Se o individuo tem 18
    elif i == 18:
        #Mostre que chegou a hora
        print('Está na hora de se alistar meu jovem !')
    #Se ele tiver mais que 18
    else:
        #Mostre que já passou da hora
        print('Já passou do tempo lek...')
        #Variavel para saber quanto tempo passou
        f = i - 18
        #Se o tempo que passou for igual a 1
        if f == 1:
            #Mostre que era pra ter se alistado a 1 ano atrás
            print(f'Era pra você ter se alistado a {f} ano atrás.')
        #Se o tempo que passou for maior que 1
        elif f > 1:
            #Mostre a quantos anoS era pra ele ter se alistado 
            print(f'Era pra você ter se alistado a {f} anos atrás.')
else:
    print('Opção Inválida, tente novamente.')
#Cabeçalho do fim do programa
print('-=-'*10, 'END', '-=-' *10)
#
    