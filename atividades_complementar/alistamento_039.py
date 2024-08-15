''' Faça um programa que leia o ano de nascimento 
de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo de alistamento 

Seu programa também deverá mostrar o tempo que falta 
ou que passou do prazo 
'''

from datetime import date
atual = date.today().year
ano_nascimento = int(input("Informe seu ano de nascimento: "))
idade = atual - ano_nascimento

print("Quem nasceu em {} tem {} anos em {}".format(ano_nascimento, idade, atual))
if idade == 18:
     print("Ja é hora de se alistar")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda vai se alistar, faltam {} anos".format(saldo))
    ano = atual + saldo
    print("seu alistamento será em {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Ja passou da hora de se alistar, você deveria ter se alistado há {} anos".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))