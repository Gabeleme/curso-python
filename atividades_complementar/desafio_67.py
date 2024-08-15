''' faça um programa que mostre a tabuada de varios números
um de cada vez para cada valor digitado pelo usuario
O programa será interrompido quando o número
solicitado for negativo '''

while True:
    numero = int(input("Digite um número para ver sua tabuada (negativo para parar): "))
    
    if numero < 0:
        break
    
    print(f"\nTabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()  # Linha em branco para separar as tabuadas

print("Programa encerrado.")