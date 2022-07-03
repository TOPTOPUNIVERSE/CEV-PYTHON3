c = to = mc = mb = 0 #Variaveis de preço,total,mais caro e mais barato recebem 0
nmb = ''
while True:
    print('~'*25, 'LOJA SUPER BARATINHO', '~'*25) #Cabeçalho
    n = str(input('Digite o nome do produto: ')) #Solicitando nome do produto
    p = float(input('Digite o preço do produto:R$'))#Solicitando preço do prodto
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()
    c += 1 #Contador
    to += p #Variavel de total somando os produtos
    while resp not in 'SN': #Caso dados inválidos
        resp = str(input('Quer continuar [S/N]: ')).strip().upper() #Solicite novamente 
    if c == 1 or p < mb:
        mb = p #Produto atual agora é o produto mais barato registrado
        nmb = n #Variavel 'nome do mais barato do produto' recebe o nome do produto atual
    if p > 1000:
        mc += 1 #Variavel mais caro contabilizando produtos acima de 1000
    if resp == 'N':
        break
print('-='*35) #Cabeçalho
print(f'O total da compra foi {to}\nTemos {mc} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nmb} que custa R${mb:.2F}')
print('-='*15, 'FIM', '-='*15)