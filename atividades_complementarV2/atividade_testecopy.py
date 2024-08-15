estado = dict() #criando um dicionario 
brasil = list() #criando uma lista

for c in range(0, 3): 
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #adiciona uma copia do dicionario na lista 
for e in brasil: #para cada estado(e) em brasil
    for k, v in e.items(): # para cada chave e valor em (e)stado 
        print(f'O campo {k} tem valor {v}')


