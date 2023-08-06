"""

Desafio 102

Crie uma função chamada fatorial() que receba dois parâmetros: o primeiro deve 
receber um número para calcular e o outro será chamado show, que será um valor 
lógico opcional, indicando se será mostrado ou não na tela o processo do calculo
do fatorial."""


def fatorial(n, show=False):
    """-> Calcula o Faorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatoral de um número n.
    """
    print('-'*45)
    f = 1
    if show == True:
        while n > 0:
            print(n, end='')
            if n > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
            f *= n
            n -= 1
        return f
    else:
        for c in range(n, 0, -1):
            f *= n
            n -= 1
        return f


# Programa principal
print(fatorial(5))
# help(fatorial)
