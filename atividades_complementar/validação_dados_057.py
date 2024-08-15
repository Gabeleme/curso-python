''' Faça um programa que leia o sexo de uma pessoa
mas so aceite os valores M ou F. caso esteja errado peça
para que digite novamente ate ter um valor correto'''

sexo = str(input("informe seu Sexo [F]eminino ou [M]asculino: "))
while sexo not in 'MmFf':
    sexo = str(input("Por favor digite seu Sexo [F]eminino ou [M]asculino: "))
    
print(f"Obrigada por informar!, seu sexo {sexo} foi registrado com sucesso")