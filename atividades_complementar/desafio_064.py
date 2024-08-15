''' Crie um programa que leia varios números inteiros
pelo teclado O programa so vai parar quando o usuario
digitar o valor 999. que é a condição de parada 
No final mostre quantos numeros foram digitados e qual
foi a soma entre eles'''

s = 0

while True:
    num = int(input("Informe um valor inteiro: "))
    if num == 999:
        break
    s += num
print(f"A soma entre os valores tem como resultado {s:.2f}")    
