# Faça uma tabuada com o valor inserido pelo usuario 

# 1 - sem guardar em variaveis 
num = int(input("Digite um numero: "))
print('-' * 12)
# tem essa forma de fazer passando o valor dentro do format 
print('{} X {} = {}'.format(num, 1, num*1))
# e dessa forma a onde vc insere o valor como string ali sem passar ele dentro do format
print('{} X 2 = {}'.format(num, num*2))

print('{} X {} = {}'.format(num, 3, num*3))
print('{} X {} = {}'.format(num, 4, num*4))
print('{} X {} = {}'.format(num, 5, num*5))
print('{} X {} = {}'.format(num, 6, num*6))
print('{} X {} = {}'.format(num, 7, num*7))
print('{} X {} = {}'.format(num, 8, num*8))
print('{} X {} = {}'.format(num, 9, num*9))
print('{} X {} = {}'.format(num, 10, num*10))
print('-' * 12)

#----------------------------------------------------------------------

'''existe duas formas de fazer, uma a onde vamos guardar o valor em variaveis
e outra mais simples que não vamos guardar em variaveis 
pois não vamos utilizar novamente

----------------------------------------
2 - guardando em variaveis 

n = int(input("Digite um numero: "))
vezes1 = n*1
vezes2 = n*2 
vezes3 = n*3
vezes4 = n*4
vezes5 = n*5
vezes6 = n*6
vezes7 = n*7
vezes8 = n*8
vezes9 = n*9
vezes10 = n*10 

print('{} X 1 = {}'.format(n, vezes1))
print('{} X 2 = {}'.format(n, vezes2))
print('{} X 3 = {}'.format(n, vezes3))
print('{} X 4 = {}'.format(n, vezes4))
print('{} X 5 = {}'.format(n, vezes5))
print('{} X 6 = {}'.format(n, vezes6))
print('{} X 7 = {}'.format(n, vezes7))
print('{} X 8 = {}'.format(n, vezes8))
print('{} X 9 = {}'.format(n, vezes9))
print('{} X 10 = {}'.format(n, vezes10))


'''

