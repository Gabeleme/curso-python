'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionario se por acaso a CTPS for diferente
de zero, o dicionario receberá também o ano de contratação e o sálario. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar'''

from datetime import datetime
dados = dict()
dados ['nome'] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input("Carteira de trabalho (0 não tem): "))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')