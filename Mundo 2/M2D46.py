from time import sleep #Importando biblioteca de tempo
print('-='*10, 'COUNTDOWN for the NEW YEAR', '-='*10) #Cabeçalho do programa
#Laço para o countdown
for c in range (10, 0, -1): #Do 10 ao 0 em ordem decrescente
    sleep(1) #Espere 1 segundo
    print(c) #Conte
sleep(0.5)
print('HAPPY NEW YEAR!!!') #Mostre na tela happy new year
print('-='*10, 'END', '-='*10) #Cabeçalho de fim do programa