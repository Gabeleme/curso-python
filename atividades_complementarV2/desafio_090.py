''' Faça um programa que leia nome e média de um aluno guardando também a situação
em um dicionario. No final mostre o conteudo da estutura na tela'''

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7: 
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-' * 20)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
    