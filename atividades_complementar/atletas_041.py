''' A confederação nacional de natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre
sua categoria de acordo com a idade

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SENIOR
- Acima: MASTER
'''

from datetime import date
atual = date.today().year
ano_nascimento = int(input("Informe seu ano de nascimento: "))
idade = atual - ano_nascimento

print("Quem nasceu em {} tem {} anos em {}".format(ano_nascimento, idade, atual))
if idade <= 9:
    print("Categoria: MIRIM")
elif idade <= 14:
    print("Categoria: INFANTIL")
elif idade <=19:
    print("Categoria JUNIOR")
elif idade == 20:
    print("Categoria SENIOR")
else:
    print("Categoria MASTER")