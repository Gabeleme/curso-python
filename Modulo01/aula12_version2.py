#-----------------------------------------------

'''
Alterando uma lista com índice

Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

#        0    1   2   3    4   5 
lista = [10, 20, 30, 40] #lista

lista[2] =  300 # alterando o valor do indice 2 para 300

del lista[2] # apaga o valor do indice 2
# depois de apagado a lista é reorganizada então os indices acabam sendo trocado

print(lista) #print pra lista completa
print(lista[2]) #print pra exibir o valor do indice escolhido

lista.append(50) #adiciona o valor escolhido ao fim da lista
lista.pop() # remove o ultimo elemento da lista 
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) #colocou ele dentro de uma variavel
print(lista, 'Removido,', ultimo_valor) 

''' se for utilizado entre a insersão do elemento ele apaga
o ultimo que foi adicionado e depois se utilizar de novo ele 
apagar o outro que se torna ultimo, igual está no exemplo de cima'''

#-----------------------------------------------

# podemos usar o valor de uma lista e colocar ele em variavel
'''
lista = [10, 20, 30, 40]
numero = lista[2]
print(numero)
'''

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