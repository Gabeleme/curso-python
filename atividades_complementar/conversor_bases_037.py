''' Escreva um programa que leia um número inteiro qualquer e peça para
o usuario escolher qual será a base de conversão:
- 1 para binario
- 2 para octal
- 3 para hexadecimal 
'''
num = int(input("Informe um número inteiro: "))
print("Escolha qual base de conversão deseja:")
base = int(input("1-binário, 2-octal, 3-hexadecimal: "))

if base == 1:
    resultado = bin(num)[2:]
    print(f"O número {num} em binário é: {resultado}")
elif base == 2:
    resultado = oct(num)[2:]  
    print(f"O número {num} em octal é: {resultado}")
elif base == 3:
    resultado = hex(num)[2:]  # Remove o prefixo '0x'
    print(f"O número {num} em hexadecimal é: {resultado}")
else: 
    print("Escolha inválida!")
    