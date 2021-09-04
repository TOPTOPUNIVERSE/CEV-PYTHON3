"""
Prática de variaveis e operadores aritméticos 
baseada no exercicio anterior"""

# Solicitando um valor
n1 = int(input('Digite um valor: \033[1;31m '))
# Solicitando outro valor
n2 = int(input('\033[mDigite outro valor: \033[1;31m '))
# Variável da soma
s = n1 + n2
# Variável da multiplicação
m = n1 * n2
# Variável da divisão
d = n1 / n2
# Variável da divisão inteira
di = n1 // n2
# Variável da exponenciação (ou potenciação)
e = n1 ** n2
# Mostrando na tela o resultado das contas
print(
    f'\033[mA soma é: \033[1;36m{s}\033[m, \n O produto é: \033[1;36m{m}\033[m, \n A divisão é: \033[1;36m{d:.3f}\033[m',
    end=' ')
# Mostrando na tela o resultado da divisão e da potência
print(f'\n A divisão inteira é: \033[1;36m{di}\033[m\n A potência é: \033[1;36m{e}\033[m')
#
# Utilizamos do código: \033[1;31m \033m para dar cor vermelha aos valores inseridos
# Utilizamos do código: \033[1;36m \033[m para dar cor cyan aos valores computados
# Utilizamos do código: :.3f para limitar a 3 casas decimais.
# Utilizamos do código: end='' para não haver quebra de linha.
# Utilizamos do código: \n para criar novas quebras de linha
