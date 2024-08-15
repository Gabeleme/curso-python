''' Crie um programa que leia nome, sexo e idade de varias pessoas
guardando os dados de cada pessoa em um dicionario e todos os 
dicionarios em uma lista. No final mostre: 

a - Quantas pessoas foram cadastradas
b - A média de idade do grupo
c - Uma lista com todas as mulheres
d - Uma lista com todas as pessoas com idade acima da média'''

galera = list()
pessoa = dict()
soma = 0
media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F ')
    pessoa['idade'] = int(input('Idadde: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-' * 20)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A médoa de idade é de {media:5.2f} anos ')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if pessoa['sexo'] in 'fF':
        print(f'{pessoa["nome"]} ', end='')
print()
print("Lista das pessoas acima da média: ")
for p in galera:
    if pessoa['idade'] >= media:
        print('   ')
        for k,v in pessoa.items():
            print(f'{k} = {v} ', end='')
        print()
print('--ENCERRADO--')
