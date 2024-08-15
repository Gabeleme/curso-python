
num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))

while True:
    print('---------------------------------\n'
          'Calculadora: \n'
          '1 - Somar os valores (+)\n'
          '2 - Multiplicar os valores (*)\n'
          '3 - Subtrair os valores (-)\n'
          '4 - Finalizar\n'
          '---------------------------------')
    resposta = int(input("Informe o que deseja realizar (use os numeros): "))
    if resposta == 1:
        soma = num1 + num2 
        print(f'A soma do valor {num1} + {num2} tem como resultado {soma}')
    elif resposta == 2:
        mult = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} tem como resultado {mult}')
    elif resposta == 3:
        sub = num1 - num2
        print(f'A subtração entre {num1} e {num2} tem como resultado {sub}')
    else:
        break
print('Fim do programa')

