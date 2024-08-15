''' Crise um algoritmo que leia um número e mostre seu 
DOBRO, TRIPLO e RAIZ QUADRADA '''

num = int(input("Digite um número inteiro: "))

dobro = num * 2
tri = num * 3
raiz = num ** (1/2)

print('O numero digitado foi {}'.format(num))
print('O dobro de {} vale {}'.format(num, dobro))
print('O triplo de {} vale {}'.format(num, tri))
print('A raiz quadrada de {} vale {}'.format(num, raiz))