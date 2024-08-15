''' Faça um programa que leia um angulo qualquer e mostre na sua tela
o valor do seno, cosseno e rangente desse angulo'''

from math import radians, sin, cos, tan
angulo = float(input("digite o angulo que vc deseja: "))
seno = sin(radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo, tangente))

'''
math - biblioteca usada em matematica 
radians - converte um ãngulo de graus para radiano
sin - calcula o seno de um ângulo dado em radianos.
cos - calcula o cosseno de um ângulo dado em radianos
tan -  calcula a tangente de um ângulo dado em radianos.
'''