exp = str(input('Digite a expressão: ')) #Solicitando expressão
pilha = [] #Lista para os parentêses
for símb in exp: #Validando os parentêses
    if símb == '(': #Se achar um ( adicione-o a lista
        pilha.append('(')
    elif símb == ')': #Se achar um ) retire o último elemento da lista 
        if len(pilha) > 0: #apenas se ela não estiver vazia
            pilha.pop()
        else: #Se estiver vazia
            pilha.append(')') #adicione-o
            break 
if len(pilha) == 0: #Se a lista estiver vazia
    print('Sua expressão está válida!')
else: 
    print('Sua expressão está errada!')