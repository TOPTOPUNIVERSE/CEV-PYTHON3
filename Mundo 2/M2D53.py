print('>'*10, 'Detector de Palíndromo', '<'*10)#Cabeçalho
f = str(input('Digite algo: ')).strip().upper()#Solicitando texto
p = f.split() #Variavel de separação
t = ''.join(p) #Variavel para juntar tudo
i = t[::-1] #Varrer a str ao contrário
'''i = '' #Variavel para tirar os espaços
for l in range(len(t) -1, -1, -1):
    i += t[l]'''
print(f'Você digitou: {f.capitalize()}')
if i == t:
    print(f'\nE ao contrário é {f.capitalize()}, Logo é Palíndromo !')
else:
    print(f'\nE ao contrário é {i}, Portanto NÃO é Palíndromo.')
print('>'*20, 'END','<'*20)#Cabeçalho
#Opção mais enxuta
'''f= str(input("Qual a frase? ")).upper().replace(" ", "")
if f == f[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")'''