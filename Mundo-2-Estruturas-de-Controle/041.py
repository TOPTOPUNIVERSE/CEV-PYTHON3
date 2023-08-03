#Importando a biblioteca de tempo para sempre rodar a data correta
from datetime import date
#Cabeçalho do programa
print('>'*10, 'Categoria de atletas de natação','<'*10)
#Solicitando o ano de nascimento
a = int(input('Informe o ano de nascimento: '))
#Variavel para calcular o ano atual
y = date.today().year
#Variavel para calcular a idade
i = y - a
#Mostrando a idade do atleta
print(f'Você tem {i} anos de idade.')
#Se a idade for igual ou menor a 9
if i <= 9:
    #Mostre a categoria mirim
    print('Você tem idade para ser um campeão de natação mirim.')
#Se a idade for igual ou menor que 14
elif i <= 14:
    #Mostre a categoria infantil
    print('Você tem idade para ser um campeão infantil de natação.')
#Se a idade for igual ou menor a 19
elif i <= 19:
    #Mostre a categoria junior
    print('Você tem idade para ser um campeão de natação junior.')
#Se a idade for igual ou menor a 20
elif i <= 25:
    #Mostre a categoria sênior
    print('Você tem idade para ser um capeão sênior de natação.')
#Se a idade for maior que as anteriores     
else:
    #Mostre a categoria master
    print('Você tem idade não para ser um campeão, mas sim um MASTER em natação.')
#Cabeçalho de fim do programa
print('>'*10, 'END','<'*10) 
