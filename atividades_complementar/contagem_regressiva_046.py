'''Faça um programa que mostre na tela uma contagem regressiva para o
estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre elas'''

from time import sleep
for cont in range(10, -1, -1): #vai contar de trás para frente
    print(cont)
    sleep(1)
print("FELIZ ANO NOVO")
''' começa no 10 e quer que conte até o 0, mas se 
passar o 0 ali ele vai contar até 1 apenas, então
colocamos o -1 para que ele possa ir até o 0 e o
outro -1 está falando que é pra ele retirar um a cada
interação, nesse caso ele vai contar de 10 até 0
de trás para frente sempre retirando 1 do valor'''