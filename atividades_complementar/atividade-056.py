''' Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas, no final do programa mostre:

- A media de idade do grupo 
- Qual o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos 
'''

id = 0
maioridadehomem = 0 
nomemaisvelho = ''
menorquevinte = 0 

for c in range (1,5):
    print('-------- {} PESSOA --------'.format(c))
    nome = str(input("Informe seu nome: ")).strip()
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Informe seu sexo [M]asculino ou [F]eminino: ")).strip()

    id += idade
    if c == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        menorquevinte += 1

media = id / 4 

print("A média entre as idade é {:.2f}".format(media))
print("O nome do homem mais velho é {} e ele tem {} anos".format(nomemaisvelho, maioridadehomem))
print("Existe {} mulheres com menos de 20 anos".format(menorquevinte))
