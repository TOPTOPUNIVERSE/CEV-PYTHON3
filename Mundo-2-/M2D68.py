from random import randint #Importando biblioteca random
print('-='*25) #Cabeçalho
print(' '*10,'BORA JOGAR PAR OU ÍMPAR?',' '*10)
print('-='*25)
historico = 0 #Variavel do historico de vitórias recebe 0
while True:
    n = int(input('Digite um valor: ')) #Solicitando valor
    print('-='*25) #Cabeçalho 
    p_i = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0] #Solicitando par ou ímpar
    while p_i not in 'PI': #Caso dados inválidos
        p_i = (input('Par ou Ímpar? [P/I]: ')).strip().upper()[0] #Solicite novamente
    print('-'*45)
    pcn = randint(0, 10) #Variavel de aleatoriedade do pc
    to = n + pcn #Variavel do total dos números somados
    res = to % 2  #Varíavel do resto da divisão dos números somados
    print(f'Você jogou {n} e eu {pcn}',end='. ') 
    if res == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    if p_i == 'P' and res == 0:
        print(f'Total de {to}, deu {resultado}!')
        print('>'*45)
        print(f'Parabéns você VENCEU!!')
        historico += 1 #Variavel de contabilização de vitórias
        print(f'Você ganhou {historico} vezes seguidas!')
        print('>'*45)
        print('Bora mais uma vez, dessa vez eu te derroto...')
        print('-'*45)
    elif p_i == 'I' and res != 0:
        print(f'Total de {to}, deu {resultado}!')
        print('>'*45)
        print(f'Parabéns você VENCEU!!')
        historico += 1 #Variavel de contabilização de vitórias
        print(f'Você ganhou {historico} vezes seguidas!')
        print('Vamos de novo? aposto que não ganha 2 vezes')
    else:
        print(f'Total de {to}, deu {resultado}!')
        print('<'*45)
        print('Você PERDEU !')
        break
    





