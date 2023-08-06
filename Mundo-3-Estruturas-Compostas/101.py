"""

Desafio 101

Crie uma função chamada voto() que vai receber como parâmetro o ano de nascimento de
uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, 
opcional ou obrigatório nas eleições."""


def voto(nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nasc
    print(f'Com {idade} anos: ', end="")
    if idade >= 18 and idade <= 65:
        return f"VOTO OBRIGATÓRIO."
    elif idade >= 16 and idade < 18 or idade > 65:
        return f"VOTO OPCIONAL."
    elif idade < 16:
        return f"NÃO VOTA."


print('-'*45)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
