n = str(input('Qual é o seu nome? '))
if n == 'Luis':
    print('Que nome bonito!')
elif n == 'pedro' or n == 'maria' or n == 'paulo':
    print('Seu nome é bem popular no Brasil')
elif n in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom-dia, {n} ! ')