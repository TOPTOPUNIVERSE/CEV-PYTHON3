print('~'*27, 'Sequência de Fibonacci','~'*27) #Cabeçalho
n = int(input('Quantos termos você quer mostrar? ')) #Solicitando termos
t1 = 0 #Variavel do 1° termo
t2 = 1 #Variavel do 2° termo
print('-'*65) #Cabeçalho
print(t1,' > ',t2,end=' > ') #Mostrando 1° e 2° termo na tela
c = 3 #Variavel de contador 
while c <= n: #Enquanto variavel c for menor ou igual ao número solicitado
    fn = t1 + t2 #Variavel fibonacci
    print(fn,end=' > ') #Mostre na tela a variavel fibonacci
    t1 = t2 #Atualize a variavel t1 
    t2 = fn #Atualize a variavel t2
    c += 1 #Contabilize uma volta
print('FIM') #Cabeçalho
print('-'*65) #Cabeçalho
print('~'*65) #Cabeçalho





    

     
      

     
     
     
    


