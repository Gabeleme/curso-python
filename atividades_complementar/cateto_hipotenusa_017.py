''' Faça um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triangulo retangulo, 
calcule e mostre o comprimento da hipotenusa '''

from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))

'''é usada para calcular a hipotenusa de um triângulo retângulo 
dado seus dois lados. Basicamente, ela calcula a raiz quadrada da 
soma dos quadrados dos seus argumentos, ou seja, para x e y '''
