"""
Desafio 022
Problema: Crie um programa que leia o nome completo de uma pessoa
          e mostre:
              - O nome com todas as letras maiúsculas e minúsculas.
              - Quantas letras ao todo(sem considerar espaços)
              - Quantas letras tem o primeiro nome."""

n = str(input('Digite seu nome completo: ')).strip()
print(f'Este é seu nome em maiúsculas: {n.upper()}'
      f'\nEste é seu nome em minúsculas: {n.lower()}')
print(f'Seu nome tem ao todo {(len(n)-n.count(" "))} letras.')
#print(f'Seu primeiro nome tem {n.find(" ")} letras. ')
s = n.split()
print(f'Seu primeiro nome é {s[0]} e ele tem {(len(s[0]))} letras.')
