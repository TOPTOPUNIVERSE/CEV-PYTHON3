"""

Desafio 105

Crie uma função chamada notas() que possa receber várias notas de alunos e retorne
um dicionário com as seguintes informações: Quantidade de notas, A maior nota,
A menor nota, A média da turma e A situação(sendo está opcional). Adicione também 
as docstrings da função."""


def notas(*núm, sit=False):
    """ -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-'*65)
    valores = {}
    if len(núm) != 0:
        valores["Total"] = len(núm)
        valores["Maior"] = max(núm)
        valores["Menor"] = min(núm)
    valores["Média"] = sum(núm) / len(núm)
    if sit == True:
        if valores["Média"] >= 7:
            valores["Situação"] = 'BOA'
        elif valores["Média"] >= 6 and valores["Média"] < 7:
            valores["Situação"] = 'Razoável'
        else:
            valores["Situação"] = 'Ruim'
    return valores


resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
help(notas)
print(resp)
