
'''
Inserindo item na lista com Insert 

Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

#         0---1---2---3    indice
lista = [10, 20, 30, 40] #lista

lista.append('Gabriela') # adicionando ao final da lista
nome = lista.pop() # removendo o ultimo 
print(lista, nome) # exibindo a lista e o que foi apagado
lista.append(1234) 
del lista [-1] # deleta o valor que se encontra no indice indicado
# lista.clear() limpa a lista
lista.insert(0, 5) 
''' O primeiro valor que passamos no insert é o indice que
queremos alterar e depois passamos o valor que queremos que 
seja adicionado a esse indice '''
print(lista[4])

# --------------------------------------

# Concatenando e estendendo listas 

lista_a = [1, 2, 3] #lista a 
lista_b = [4, 5, 6] #lista b

# lista c recebe a junção da lista a com a lista b
lista_c = lista_a + lista_b

# vai alterar a lista a, e vai extender da lista b
lista_a.extend(lista_b) 

print(lista_a) # imprime na tela 

