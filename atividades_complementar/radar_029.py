'''
faça um programa que leia a velocidade de um carro, 
se ele ultrapassar de 80km/h mostre uma mensagem dizendo que 
ele foi multado, a multa vai custar 7 reais por cada km 
acima do limite '''

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
     print('Você ultrapassou o limite de velicidade, MULTADO') 
     multa = (velocidade - 80) * 7
     print('Você terá que pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')