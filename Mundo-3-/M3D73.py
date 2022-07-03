brasileirao = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo',
            'Athletico-PR', 'Ceará SC', 'Santos', 'Atlético-GO', 'Bahia', 
            'Internacional','Corinthians', 'Fluminense', 'Juventude', 'Sport Recife',
            'São Paulo', 'América-MG','Cuiabá', 'Grêmio', 'Chapecoense')
print('-='*14,'Tabela do Brasileirão','-='*14) #Cabeçalho
print(f'Os 5 primeiros colocados são: {brasileirao[:5]}')
print('--'*40)
print(f'Os últimos 4 colocados da tabela são: {brasileirao[-4:]}')
print('--'*40)
print(f'Os times da tabela em ordem alfabética: {sorted(brasileirao)}')
print('--'*40)
print(f'O time Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição')