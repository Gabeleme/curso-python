'''Desenvolva um programa que pergunte a distancia de uma viagem 
em Km. Calcule o preço da passagem cobrando R$0,50 por Km 
para viagens de até 200Km e R$0.45 para viagens mais longas
'''

distancia = float(input("Qual a distancia da viagem? "))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else: 
    preco = distancia * 0.45
print("O preço da sua viagem será de R$ {:.2f}".format(preco))