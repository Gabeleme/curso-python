'''
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índice e fatiamento  
Métodos úteis: append, insert, pop, del, clear, extends...
'''
#-----------------------------------------------

#------- +01234
#------- -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista)

#-----------------------------------------------
#                   INDICES 
#         0    1        2            3    4
#        -5   -4       -3           -2   -1

lista = [123, True, 'Luiz Otávio',  1.2, []] #dentro da lista pode existir outra lista
     #   int  boll    string       ponto flutuante
lista[-3] = 'Maria'  # mudando o que está no indice -3 sendo alterado de Luiz para maria
print(lista)
print(lista[2], type(lista[2]))

#-----------------------------------------------

'''
- Lista é um dado mutável por que quando temos uma lista com 
vários valores e queremos alterar esses valores é possível 
fazer essa alteração. 

- Fazemos essa alteração passando o índice da posição e
passando o que queremos colocar no lugar, temos que lembrar
que na programação sempre contamos o 0, então não podemos 
se esquecer que ao contar o indice ele sempre vai começar do 0
e quando for negativo ele começa do -1 pois o 0 ja vale pro
positivo e para o negativo 
'''

#-----------------------------------------------



