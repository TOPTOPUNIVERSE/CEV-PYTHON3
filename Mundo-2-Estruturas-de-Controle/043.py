#Cabeçalho do programa
print('-_-'*10,'Cálculo de IMC', '-_-'*10)
#Solicitando o peso
p = float(input('Informe seu peso: (Kg) '))
#Solicitando a altura
a = float(input('Informe a sua altura: (m) '))
#Variavel para calcular o IMC
imc = p / (a * a)
#Mostrando o IMC
print(f'Seu Indice de massa corporal é {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso, bora comer uns lanche ai amigão.')
elif imc < 25:
    print('Peso ideal, parabéns !')
elif imc < 30:
    print('Sobrepeso, pochetinha começando a ganhar vida !')
elif imc < 40: 
    print('Obesidade, ai não dá né pochetinha já com toda sua família.')
else:
    print('Obesidade mórbida, vai morre se continuar assim amigão..')
#Cabeçalho de fim do programa
print('-_-'*10, 'END', '-_-'*10)
#
