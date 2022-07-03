'''lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
# Tuplas são imutáveis
lanche [1] = 'Refrigerante'
print(lanche)
#retorna o erro:  lanche [1] = 'Refrigerante'
TypeError: 'tuple' object does not support item assignment'''
#
#lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#for comida in lanche:
#    print(f'Eu vou comer {comida}')
#print('Comi pra caramba !')
#Outra forma de utilizar o for
#lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#for cont in range(0, len(lanche)):
 #   print(f'Eu vou comer {lanche[cont]}')
#print('Comi pra caramba !')
#Formas de utilizar o for e mostrar a posição na tulipa
#lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#print('Comi pra caramba !')
#OU
#lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#for pos,comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')
#print('Comi pra caramba !')
#Para mostrar a  tulipa em ordem alfabética
#lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#print(sorted(lanche))
#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = a + b
#print(c)
#print(len(c)) #Para mostrar a quantidade de elementos
#print(c.count(4)) #Para ver quantas vezes apareceram 4 na tulipa
#print(c.index(8)) #Para mostrar em que posição está o número 8
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)