"""

Desafio 106

Crie um mini-sistema que utilize o Interactive Help do Python. O usuário vai
digitar o comando e o manual vai aparecer. Quando o usuário digitar 'FIM', o
programa se encerrará. Utilize cores! """

from time import sleep


def busca():
    titulo = f"Acessando o manual do comando: {pergunta.capitalize()}"
    tam = len(titulo) + 4
    sleep(1)
    print('\033[0;30;43m')
    print('-' * tam)
    print(f"{titulo:^{tam}}")
    print("-" * tam)
    sleep(1)
    return(help(pergunta.lower()))


def cabecalho(msg):
    tam = len(msg) + 4
    print('\033[0;30;41m')
    print('='*tam)
    print(f'{msg:^{tam}}')
    print('='*tam)
    print('\033[m')
    sleep(0.5)


# Programa principal
while True:
    cabecalho('SISTEMA DE AJUDA PyHelp')
    pergunta = str(input('\033[0;33;40mDigite a Função ou a Biblioteca:  ')).strip()
    if pergunta.upper() in 'FIM':
        print('\033[0;30;41m')
        cabecalho = 'FIM'
        tam = len(cabecalho)+4
        print('='*tam)
        print(f'{cabecalho:^{tam}}')
        print('='*tam)
        print('\033[m')
        break
    else:
        busca()
