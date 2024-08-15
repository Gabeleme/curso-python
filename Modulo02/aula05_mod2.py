# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Gabriela Oliveira',
    'sobrenome': 'Leme',
    'idade': 19,
}

print(len(pessoa)) #quantidade de chaves
print(list(pessoa.keys())) # quando queremos ver as chaves
print(list(pessoa.values())) # quando queremos ver o valor
print(list(pessoa.items())) # quando queremos ver tanto a chave quanto o valor
