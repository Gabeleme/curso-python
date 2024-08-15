''' Faça um programa que leia o nome compelto de uma pessoa
mostrando em seguida o primeiro e o último nome separadamente '''

n = str(input('Qual seu nome? ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))