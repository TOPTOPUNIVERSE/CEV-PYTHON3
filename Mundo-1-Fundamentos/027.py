"""""
Desafio 027
Problema: Faça um programa que leia o nome completo de uma
          pessoa, mostrando em seguida o primeiro e o último
          nome separadamente."""

# Solicitando nome completo
n = str(input('Digite seu nome completo:\033[1;32m ')).strip().capitalize()
# Variável para separar o nome
n2 = n.split()
# Mostrando na tela mensagem de prazer em te conhecer fulano
# Mostrando também o primeiro e último nome do ciclano
print(f'\033[mMuito prazer em te conhecer!\n'
      f'Seu primeiro nome é:\033[1;34m {n2[0]}\033[m\n'
      f'Seu último nome é:\033[1;34m {n2[len(n2)-1]}\033[m')
#
# Para cor verde no nome inserido: \033[1;32m
# Para cor azul no primeiro e último nome: \033[1;34m
