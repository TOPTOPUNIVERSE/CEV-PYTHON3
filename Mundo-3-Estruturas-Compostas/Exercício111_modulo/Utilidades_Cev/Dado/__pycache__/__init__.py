"""

Desafio 112 (Sim 112 na pasta do 111)

Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado
dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a fun-
-ção input(), mas com uma validação de dados para aceitar apenas valores que sejam
monetários."""


def leiaDinheiro(pergunta):
    while True:
        valor = str(input(pergunta)).replace(',', '.')
        if valor.replace('.', '').strip().isnumeric() == True:
            valor = float(valor)
            break
        else:
            print(f'\033[1;1;31mERRO: "{valor.strip()}" é um preço inválido!\033[m')
    return valor
