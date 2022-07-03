# Prática de def e funções

# def titulo(txt):
# print('-='*20)
# print(txt)
# print('-='*20)


# Programa principal
#titulo('  CURSO EM VÍDEO  ')
#titulo('   Luis Augusto   ')
#titulo('  Aprenda python  ')

# def soma(a, b):
# s = a + b
#print(f"A soma entre {a} e {b} é igual a {s}.")


# Programa principal
#a = 4
#b = 5
#s = a + b
# print(s)
# Simplificando com def
# soma(4, 5)#Sempre nessa ordem em que a 1 ocorrencia vai para o primeiro parâmetro
# ou seja, 4 para A assim como 5 Para B

#a = 8
#b = 9
#s = a + b
# print(s)
# Simplificando com def
# soma(8, 9)#Sempre nessa ordem em que a 1 ocorrencia vai para o primeiro parâmetro
# ou seja, 8 para A assim como 9 Para B

#a = 2
#b = 1
#s = a + b
# print(s)
# Simplificando com def
# soma(2, 1) #Sempre nessa ordem em que a 1 ocorrencia vai para o primeiro parâmetro
# ou seja, 2 para A assim como 1 Para B

# Especificando o parâmetro do def

# def soma(a, b):
#print(f"A = {a} e B = {b}")
#s = a + b
#print(f"A soma entre {a} e {b} é igual a {s}.")


# Programa principal
# soma(b=4, a=5)  # não necessariamente nessa ordem, podendo ser assim: (a=4, b=5)
# soma()

# Empacotando parâmetros com def e fazendo contador

# def contador(*núm):
#    print(núm) #sendo este uma tupla
#
#
#contador(5, 7, 3, 1, 4)
#contador(8, 4, 7)


# Prática de def com for
# def contador(*núm):
#    for valor in núm:
#        print(f'{valor} ', end=' ')
#    print('FIM')
#
#
#contador(5, 7, 3, 1, 4)
#contador(8, 4, 7)


# Prática com def e len
# def contador(*núm):
#    tam = len(núm)
#    print(f'Recebi os valores {núm} e são ao todo {tam} números.')
#
#
#contador(5, 7, 3, 1, 4)
#contador(8, 4, 7)

# Prática com def e lista

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa principal
valores = [1, 4, 6, 1, 5, 6]
dobra(valores)
print(valores)
