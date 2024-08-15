''' Crie um programa que leia varios números inteiros
pelo teclado, no final da execusão mostre a média
entre todos os valores e qual foi o maior
e o menor valores lidos. o programa deve perguntar
ao usuario se ele quer ou não continuar a digitar valores '''


soma = 0
contador = 0
maior = 0
menor = 0
media = 0
p = 'S'

while p in 'Ss':
    num = int(input("Informe um valor inteiro: "))
    soma = soma + num
    contador +=1
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    p = str(input("deseja continuar [S]im ou [N]ão: ")).strip().upper()[0]
media = soma / contador   
print(f"A media entre os valores foi {media}")
print(f"O maior valor foi {maior} e o menor valor foi {menor}")



