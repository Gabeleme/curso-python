# faça um programa que leia quanto de dinheiro uma pessoa tem e mostre quantos dolares ela pode comprar 
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.49
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar ))