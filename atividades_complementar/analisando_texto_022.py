'''
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiusculas
- O nome com todas as letras minusculas
- Quantas letras ao todos (sem considerar espaços)
- Quantas letras tem o primeiro nome
'''

nome = str(input("Informe seu nome completo: ")).strip()
print("Seu nome com todas as letras maiusculas vai ficar {}".format(nome.upper()))
print("seu nome com todas as letras minusculas vai ficar {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)-nome.count(' ')))
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))
