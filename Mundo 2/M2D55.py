print('>'*10,'Quem pesa mais??', '<'*10)#Cabeçalho
ma = 0 #Variavel de maior peso
me = 0 #Variavel de menor peso
for c in range(1, 6): 
    p = float(input('Digite seu peso: ')) #Solicitando peso
    if p == 1: #Se o peso for igual a 1
        ma = p #Defina maior peso como 1
        me = p #Defina menor peso como 1
    else: 
        if p > ma: #Se peso for maior que o maior peso registrado
            ma = p #Defina valor de peso atual como o maior peso registrado
        #Se o menor peso é igual a 0 ou o peso atual é menor 
        #que o menor peso registrado 
        if me == 0 or p < me: 
            me = p #Defina o valor do peso atual como o menor peso registrado
print(f'O maior peso registrado foi: {ma}Kg.\nE o menor peso foi: {me}Kg.')



