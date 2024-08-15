''' Uma empresa contrata um encanador a R$ 35.00 por dia. Crie um 
programa que solicite o número de dias trabalhados pelo encanador e 
mostre o valor líquido a ser pago, sabendo que são descontados 8% de 
imposto de renda. '''

dias_trabalhados = int(input("Informe quantos dias foram trabalhados: "))
valor_bruto = dias_trabalhados * 35 
imposto = valor_bruto * 0.08
valor_liquido = valor_bruto - imposto

print(f"O valor final dos {dias_trabalhados} dias sem descontar imposto é de {valor_bruto:.2f}")
print(f"O valor final dos {dias_trabalhados} dias com o desconto do imposto é de {valor_liquido:.2f}")


