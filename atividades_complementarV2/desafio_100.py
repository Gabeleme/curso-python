''' Faça um programa que tenha uma lista chamada numeros
e duas funções chamada, sorteia() e somapar() 
A primeira função vai sortear 5 numeros e vai colocados 
dentro de uma lista e a segunda função vai mostrar a soma 
entre todos os valores pares sorteados pela função anterior'''

from random import randintn
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randintn(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto')

def somaPar(lista):
    soma = 0
    for valor in lista: 
         if valor % 2 ==0:
             soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)