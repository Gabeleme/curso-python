''' Faça um programa que leia um número inteiro e 
mostre na tela o seu sucessor e seu antecessor'''

num = int(input("Digite um numero: "))

ant = num - 1
suce = num + 1

print("Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}".format(num, ant, suce))