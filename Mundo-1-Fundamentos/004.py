"""
Desafio 004
Problema: Faça um programa que leia algo pelo teclado e mostre na tela
          seu tipo primitivo e todas as informações possíveis sobre ela."""

a = input('Digite algo: ')
print(f'\033[1;34mQual o tipo primitivo desse valor?\033[m', f'\033[;1m{type(a)}')
print(f'\033[1;34mÉ um número?\033[m', f'\033[;1m{a.isnumeric()}')
print(f'\033[1;34mÉ alfanúmerico?\033[m', f'\033[;1m{a.isalnum()}')
print(f'\033[1;34mÉ um digíto?\033[m', f'\033[;1m{a.isdigit()}')
print(f'\033[1;34mContém decimais?\033[m', f'\033[;1m{a.isdecimal()}')
print(f'\033[1;34mEsta capitalizada?\033[m', f'\033[;1m{a.istitle()}')
print(f'\033[1;34mEsta em maiúsculas?\033[m', f'\033[;1m{a.isupper()}')
print(f'\033[1;34mEsta em minúsculas?\033[m', f'\033[;1m{a.islower()}')
#
# Cor azul usada nas perguntas com o código:  \033[1;34m \033[m
# Negrito usado nas respostas com o código:   \033[;1m   \033[m
