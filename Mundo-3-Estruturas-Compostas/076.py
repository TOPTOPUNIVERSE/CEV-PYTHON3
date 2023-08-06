#Tupla com os produtos e seus respectivos valores
lista = ('Pão', 1.00,'Bolacha recheada',2.50,'Refrigerante', 5.00,
        'Broa', 2.50 , 'Pão de queijo', 1.00, 'Lingua de Sogra', 1.50,
        'Sonho Tradicional', 2.00, 'Bolo de Fúba', 1.00, 'Torta salgada', 1.50)
print('='*15,'PADOCA DO SEU ZÉ','='*15) #Cabeçalho
for pos in range(0, len(lista),2): #Mostrar de 2 em 2
        print(f'{lista[pos]:.<35}',f'R${lista[pos+1]:.2f}')
print('='*45)
