#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
print('-='*10, 'Verificador de vogais na tupla','-='*10) #Cabeçalho
tupla = ('amarelo', 'azul', 'vermelho', 'verde', 'rosa', 'branco', 'aprender',
        'futuro', 'programar', 'linguagem', 'python', 'praticar')
for palavras in tupla: #Para cada palavra na tupla
    print(f'\nNa palavra {palavras.upper()} temos: ',end='')
    for letras in palavras: #Para cada letra nas palavras
        if letras.lower() in 'aeiou': #Verificação das vogais
            print(letras,end=' ')
print(' ')
print(f'-='*10,'Fim', '-='*10)