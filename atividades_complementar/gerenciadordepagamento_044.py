''' Elabore um programa que calcule o valor a ser pago por um
produto considerando o seu preço normal e condição de pagamento: 

- Á vista dinheiro/cheque: 10% de desconto
- Á vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros 
'''

preco = float(input("Informe o preço do produto: "))
print("Formas de Pagamento: ")
print("1- Á vista dinheiro/cheque (desconto de 10%)")
print("2- Á vista no cartão (desconto de 5%)")
print("3- 2x no cartão (não possui desconto)")
print("4- 3x ou mais no cartão (não possui desconto e o juros é de 20%)")
condicao_pagamento = int(input("Informe qual será a forma de pagamento: "))

if condicao_pagamento == 1:
    desconto = preco - (preco * 10 / 100)
    print("O valor do seu produto é de R$:{:.2f} mas com o desconto de ficará R$:{:.2f}".format(preco, desconto))
elif condicao_pagamento == 2:
    desconto = preco - (preco * 5 / 100)
    print("O valor do seu produto é de R$:{:.2f} mas com o desconto ficará R$:{:.2f}".format(preco, desconto))
elif condicao_pagamento == 3:
    parcela = preco / 2 
    print("Seu procuto vai ser parcelado em 2x, o valor total dele é de {} e cada parcela tem o valor de {}".format(preco, parcela))
elif condicao_pagamento == 4:
    juros = preco + (preco * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = juros / totparc
    print("Sua compra será parcelada em {}x de R$:{:.2f} com juros".format(totparc, parcela))
    print("O valor do seu produto é de R$:{:.2f} e com o juros ficará R$:{:.2f}".format(preco, juros))
else:
    print("Forma de pagamento invalida")