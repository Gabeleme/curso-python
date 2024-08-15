''' O mesmo professor do Ex anterior quer sortear a ordem de 
apresentação de trabalhos dos alunos, Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada '''

from random import shuffle
n1 = str(input("digite o nome do aluno: "))
n2 = str(input("digite o nome do aluno: "))
n3 = str(input("digite o nome do aluno: "))
n4 = str(input("digite o nome do aluno: "))
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)

'''
random - é usada para gerar números pseudoaleatórios e realizar operações que envolvem aleatoriedade.
shuffle - é usada para embaralhar os elementos de uma lista de forma aleatória. Ela modifica 
a lista original, rearranjando seus elementos de maneira aleatória. 
'''