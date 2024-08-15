'''
Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius.
A fórmula de conversão a ser utilizada pode ser C = ((F - 32) * 5) / 9, 
em que a variável F é a temperatura em graus Fahrenheit e a variável C é a temperatura em graus Celsius.
'''

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

celsius = ((fahrenheit - 32) * 5) / 9

print(f"A temperatura em graus Celsius é: {celsius:.2f}")
