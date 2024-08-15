# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira 

from math  import trunc   #para importar apenas um item da biblioteca de math
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))


 #TBM PODEMOS FAZER DESSA FORMA, colocando o int(num)
'''num = float(input('Digite um numero: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))'''  