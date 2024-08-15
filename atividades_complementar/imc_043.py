''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo

- Abaixo de 18.5: ABAIXO DO PESO
- Entre 18.5 e 25: PESO IDEAL 
- 25 até 30: SOBREPESO
- 30 até 40 OBESIDADE
- Acima de 40: OBESIDADE MÓRBIDA
'''

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("PESO IDEAL")
elif 25 <= imc < 30:
    print("SOBREPESO")
elif 30 >= imc <= 40:
    print("OBESIDADE")
else:
    print("OBESIDADE MÓRBIDA")