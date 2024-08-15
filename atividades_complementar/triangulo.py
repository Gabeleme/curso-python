'''
-----------------------------------------------------------------------------------------------------------
Exercicio 1
Determinar, dados os comprimentos dos lados de um triângulo, se o triângulo pode ser formado (se existe).
Para tanto, leia os três lados do triângulo e indique se ele é um triângulo.
Para ser um triângulo, cada lado deve ser menor que a soma dos outros dois.
----------------------------------------------------------------------------------------------------------
Exercicio 2
Supondo que os três valores informados formem um triângulo, determine se ele é equilátero.
Um triângulo equilátero é composto por todos os lados iguais.
----------------------------------------------------------------------------------------------------------
Exercicio 3
Supondo que os três valores informados formem um triângulo, determine se ele é isósceles.
Um triângulo isósceles não é equilátero, pois é composto por somente dois lados iguais.
----------------------------------------------------------------------------------------------------------
Exercicio 4
Supondo que os três valores informados formem um triângulo, determine se ele é escaleno.
Um triângulo escaleno não é equilátero, nem isósceles, pois é composto por todos os lados sendo diferentes.
------------------------------------------------------------------------------------------------------------
Exercicio 5
Usando os exercícios 1 a 4, crie um programa que determine, 
dados os comprimentos dos lados de um triângulo, se o triângulo pode ser formado (se existe) 
e qual o tipo dele (equilátero, isósceles ou escaleno).
---------------------------------------------------------------------------------------------------------------
'''

a = float(input("Informe o primeiro lado do triangulo: "))
b = float(input("Informe o segundo lado do triangulo: "))
c = float(input("Informe o terceiro lado do triangulo: "))

testar_triangulo = a < b + c and b < a + c and c < a + b
equilatero = (a == b == c) 
isoceles = a == b or b == c or a == c
escaleno = a != b and b != c and a != c

if testar_triangulo:
    print("Os lados informados formam um triângulo.")
    if equilatero:
        print("Ele é um triangulo equilatero")
    elif isoceles:
        print("Ele é um triangulo isoceles")
    elif escaleno:
        print("Ele é um triangulo escaleno")
else:
    print("Os lados informados não formam um triângulo.")
