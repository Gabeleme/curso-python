''' Crie um programa que leia varios números inteiros pelo
teclado. O programa só vai parar quando o usuario digitar 
o valor 999, que é a condição de parada. No final mostre
quantos números foram digitados e qual foi a soma entre elas'''

soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro (999 para parar): "))
    
    if numero == 999:
        break
    
    soma += numero
    contador += 1


print(f"Quantidade de números digitados: {contador}")
print(f"Soma dos números digitados: {soma}")