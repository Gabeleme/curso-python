'''Escreva um programa para aprovar o empréstimo bancário para a 
compra de uma casa. O programa vai perguntar o valor da casa, o
salario do comprador do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salario ou então o emprestimo será negado
'''

valor_casa = float(input("Qual o valor da casa R$: "))
salario = float(input("Informe seu salario R$: "))
ano_pagando = float(input("Em quantos anos pretende pagar a casa?"))
prestacao = valor_casa / (ano_pagando * 12)
minimo = salario * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(valor_casa, ano_pagando, prestacao))
if prestacao <= minimo:
    print("emprestimo APROVADO")
else: 
    print("Emprestimo NEGADO")
