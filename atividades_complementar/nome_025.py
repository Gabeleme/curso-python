''' Crie um programa que leia o nome de uma pessoa
e diga se ela tem Silva no nome'''

nome = str(input('Digite seu nome: ')).strip() #eliminar o espaço desnecessario
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) 

''' verifica se na variavel nome tem silva e converte tudo pra minusuculo 
para que não de o mesmo erro que disse no anterior, de escrever com maiusculo 
ou intercalado e ele dar a resposta errada '''