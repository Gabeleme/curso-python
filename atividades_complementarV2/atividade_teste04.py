pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22} #dicionario
print(pessoas['nome']) #imprimindo com o indice chamado nome

#imprimindo com escrita junto e quando for assim temos que usar aspas duplas
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') 

print(pessoas.values()) #imprimindo apenas os valores
print(pessoas.keys()) #imprimindo apenas as chaves
print(pessoas.items()) #imprimindo tanto o valor quanto a chave

#utilizando laço
for k, v in pessoas.items(): 
    print(f'{k} = {v}')