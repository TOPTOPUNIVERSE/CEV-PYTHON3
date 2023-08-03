#Cabeçalho do programa
print('-=-'*10, 'Calculo da média', '-=-'*10)
#Solicitando nota
n1 = float(input('Informe sua média das provas: '))
#Solicitando a segunda nota
n2 = float(input('Informe a nota de redação: '))
#Calculando a média
m = (n1 + n2 ) / 2
#Mostrando a média
print(f'Sua média é: {m:.1f}')
if 7 > m >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif m < 5:
    print('O aluno está REPROVADO.')
elif m >= 7:
    print('O aluno está APROVADO')
'''#Se a média for abaixo de 5
if m < 5.0:
    #Mostre reprovado
    print('REPROVADO')
#Se a média for menor que 6.9
elif m < 6.9:
    #Mostre recuperação
    print(f'RECUPERAÇÃO')
#Se a média for maior que 6.9
elif m > 6.9:
    #Mostre aprovado
    print('APROVADO')'''
#Cabeçalho de fim do programa
print('-=-'*10, 'END','-=-'*10)
