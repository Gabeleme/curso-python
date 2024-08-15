''' Crie um programa que leia um número real qualquer 
pelo teclado e mostre na tela sua porção inteira '''

import math #biblioteca usada em matematica 
num = float(input("Informe o valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, math.trunc(num)))

''' trunc retorna o valor sem a parte fracionada dele, fazendo com que o 
valor fique de maneira arredondada'''