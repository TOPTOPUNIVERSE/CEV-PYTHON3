print('='*10,'Mostrando números extensos de 0 a 20', '='*10) #Cabeçalho
contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
             'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
              'Dez', 'Onze', 'Doze', 'Treze' ,'Quatorze',
               'Quinze','Dezesseis','Dezessete', 'Dezoito',
                'Dezenove', 'Vinte')
while True:
     num = int(input('Digite um número entre 0 e 20: '))
     while num < 0 or num > 20: #Caso dados inválidos
          num = int(input('Digite um número entre 0 e 20: '))
     print(f'Você digitou o número {contagem[num]}')
     print('-'*45)
     continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
     while continuar not in 'SN': #Caso dados inválidos
          continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
     if continuar == 'N':
        break
print('='*25,'Fim','='*25)
