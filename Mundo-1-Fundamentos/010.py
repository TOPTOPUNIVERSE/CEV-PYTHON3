"""
Desafio 010
Problema: Crie um programa que leia quanto dinheiro uma pessoa tem
          na carteira e mostre quantos dólares(e outras moedas) ela pode comprar."""

n = float(input('Quanto eu tenho: R$'))
print(f'Com a sua quantia atual que é R${n}\nVocê pode comprar US${n/3.27:.2f} Dólares.'
      f'\nVocê pode comprar: {n/4.54:.2f} Dolares canadenses.'
      f'\nVocê pode comprar: {n/6.71:.2f} euros.')
