print('-='*10, 'TABUADA', '-='*10)#Cabeçalho
#Solicitando número para tabuada
n = int(input('Mostre a tabuada do: '))
print('-'*20)
for c in range(1, 11):#Mostrando na tela a tabuada do número inserido
    print(f'\033[1;34m {n} \033[m x \033[1;34m {c} \033[m = \033[1;33m {n * c}\033[m')
print('-'*20)
print('-='*10, 'FIM','-='*10)#Cabeçalho
#
#Para cor azul: \033[1;34m
#Para cor amarela: \033[1;33m