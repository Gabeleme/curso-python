''' Crie um programa que leia a idade e o sexo de varias pessoas
A cada pessoa cadastrada o programa deverá perguntar se 
o usuario quer ou não continuar No final mostre

- Quantas pessoas tem mais de 18 anos
_ Quantos homens foram cadastrados
_ Quantas mulheres tem menos de 20 anos 

'''
mais_de_18 = 0
homens_cadastrados = 0
mulheres_menos_20 = 0
continuar = 'S'

while continuar in 'Ss':
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Informe seu sexo [M]asculino ou [F]eminino: ")).strip()

    if idade >= 18:
        mais_de_18 +=1
    if sexo == 'M':
        homens_cadastrados += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    continuar = str(input("Deseja coninuar [s]im ou [n]ão: "))

print(f"\nQuantidade de pessoas com mais de 18 anos: {mais_de_18}")
print(f"Quantidade de homens cadastrados: {homens_cadastrados}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")