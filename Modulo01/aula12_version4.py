"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2] # lista a 

''' Ao usar o copy ele copia os dados da lista a
para a lista b e retorna os mesmos valores, porem quando
alterado algo em uma das lista não é alterada na outra '''
lista_b = lista_a.copy() 

lista_a[0] = 'Qualquer coisa' # mudando o indice 0

print(lista_a) # print na lista a
print(lista_b) # print na lista b 

# ------------------------------

# for in com listas

lista = ['Maria', 'Helena', 'Luiz'] # lista 

# para cada item (nome) na minha lista quero (passa o que quer fazer)
for nome in lista:
    print(nome, type(nome)) 
# printa a lista retornando o valor 