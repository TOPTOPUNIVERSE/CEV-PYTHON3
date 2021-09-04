# Solicitando nome
n = str(input('Qual é seu nome?\033[1;34m  '))
# Mostrando na tela mensagem de prazer em te conhecer fulano
print(f'\033[mPrazer em te conhecer \033\033[1;34m!{n:_^20}!\033[m') 
#
#Para cor azul da resposta utilizamos o código: \033[1;34m \033[m
#Para destaque do nome com 20 espaços utilizzamos o código: :_^20
