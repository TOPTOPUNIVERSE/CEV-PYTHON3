print('-='*15,'Cadastro VIP','-='*15)
vip = []
while True:
    v = int(input('Digite um número: '))
    if v in vip:
        print('Número do vip já cadastrado, não vou adicionar!')
    else:
        vip.append(v)
        print('Vip cadastrado com sucesso!')
    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if cont in 'N':
        break
print('-'*55)
print(f'Os números vip cadastrados são: {sorted(vip)}')
print('-='*15,'Fim','-='*15)