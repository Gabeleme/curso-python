'''Crie um programa que leia o ano de nascimento de 
sete pessoas. No final mostre quantas pessoas ainda 
não atingiram a maioridade e quantas que ja são maiores'''

from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range (1, 8):
    ano_nasc = int(input("Informe o ano de nascimento: "))
    idade = anoatual - ano_nasc
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('Ao todo tivemso {} pessoas maiores de idade'.format(maior))
print('E tambem tivemos {} pessoas menores de idade'.format(menor))