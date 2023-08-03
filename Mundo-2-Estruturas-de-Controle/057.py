
s = ''
while s != 'M' and s != 'F':
    s = str(input('DIgite o sexo [M/F]: ')).upper().strip()
    if s != 'M' and s != 'F':
        print('Dados inválidos.Por favor digite a letra correta!!!')
if s == 'M':
    s = 'Masculino'
else:
    s = 'Feminino'
print(f'Sexo {s} registrado com sucesso!')