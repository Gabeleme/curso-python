brasil = [] #criando uma lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'} #criando um dicionarioo
estado2 = {'uf': 'São Paulo', 'sigra': 'SP'} #criando um dicionario

brasil.append(estado1) #adicionando o dicionario na lista
brasil.append(estado2) #adicionando o dicionario na lista

print(estado1) #imprime os dados do estado 1
print(estado2) #imprime os dados do estado 2
print(brasil) #imprime a lista inteira mostrando os dois estados 
print(brasil[0]) #o que está em 0 na lista que no caso é o RJ 
print(brasil[1]) #o que está em 1 na lista que no caso é o SP
print(brasil[0]['uf'])# vai imprimir o que está no indice 0 e no uf que no caso Rio de Janeiro
print(brasil[1]['uf'])# vai imprimir o que está no indice 1 e no uf que no caso São Paulo
