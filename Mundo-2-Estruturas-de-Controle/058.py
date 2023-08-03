from random import randint  # Importando função randint da biblioteca random
from time import sleep  # Importando função sleep da biblioteca time

r = randint(0, 10) #Variável que faz o código sortear um número de 0 a 5
print('-=-'*10,'Jogo da adivinhação ','-=-'*10) #Cabeçalho do programa
#Solicitando que o jogador adivinhe um número de 0 á 5
q = int(input('Estou pensando em um número de 0 a 10, consegue adivinhar?  ')) 
#Mostrando na tela a mensagem 'Processando...' passando o conceito de vida em máquina
print('Processando...')
sleep(1)#Colocando o programa para descansar por 2 segundos.
t = 0 #Variavel de tentativas
while q != r: #Se o número inserido for diferente ao número sorteado
    t += 1 #Cada vez que o usuário errar será contabilizado uma tentativa
    if q < r: #Se o número inserido for menor que o sorteado
        print('Mais...Tente novamente.') #De uma dica
    elif q > r: #Se o número inserido for maior que o sorteado
        print('Menos...Tente novamente.') #De uma dica
    q = int(input('Estou pensando em um número de 0 a 10, consegue adivinhar?  '))
print(f'Acertou ! ! !\nCaramba você precisou de {t} tentativas para advinhar !!')
print('-=-'*10,'END GAME','-=-'*10) #Mostre na tela o cabeçalho de fim de jogo