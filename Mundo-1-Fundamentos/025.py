"""
  Desafio 025
  Problema: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome."""

# Solicitando nome completo
q = str(input('Qual é o seu nome completo?\033[1;35m ')).strip()
# Mostrando na tela se o nome tem silva
print(f'\033[mSeu nome tem Silva? {"silva"in q.lower().split()}')
#
# Para cor magenta do nome: \033[1;35m
