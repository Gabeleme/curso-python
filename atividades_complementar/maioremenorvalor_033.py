''' Faça um programa que leia 3 números e fale qual 
é o maior e qual é o menor '''

n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe um número inteiro: "))
n3 = int(input("Informe um número inteiro: "))

#verificando quem é o menor 
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3 
#verificando quem é o maior 
maior = n2 
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3 
    
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))