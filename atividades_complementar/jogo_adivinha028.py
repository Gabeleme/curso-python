''' 
Escreva um programa que faça o computador
"pensar" em um número inteiro entre 0 a 5 e peça 
para o usuario tentar descobrir qual foi 
o número escolhido pelo computador. 

O programa deverá escrever na tela se o usuario venceu ou perdeu 
'''

from random import randint
computador = randint(0, 5) #faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
jogador = int(input("em que número eu pensei? ")) #jogador tenta adivinhar
if jogador == computador:
    print("PARABÉNS! você conseguiu me vencer")
else: 
    print("GANHEI! Eu pensei no número {} e não no {}".format(computador, jogador))