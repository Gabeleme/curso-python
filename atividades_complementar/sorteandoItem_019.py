''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido'''

from random import choice
n1 = str(input("digite o nome do aluno: "))
n2 = str(input("digite o nome do aluno: "))
n3 = str(input("digite o nome do aluno: "))
n4 = str(input("digite o nome do aluno: "))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print("O aluno escolhido foi {}".format(escolhido))

''' 
random - é usada para gerar números pseudoaleatórios e realizar operações que envolvem aleatoriedade. 
choice - é usada para selecionar um elemento aleatório de uma sequência, como uma lista ou uma tupla. 
Ela retorna um único elemento escolhido aleatoriamente da sequência fornecida.
'''