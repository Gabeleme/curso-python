''' faça um program que leia um número qualquer 
e motre o seu fatorial

ex: 
5! = 5x4x3x2x1 + 120

'''

# Solicita o número para calcular o fatorial
numero = int(input("Digite um número para calcular o fatorial: "))

# Verifica se o número é negativo
if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:
    resultado = 1
    # Calcula o fatorial
    for i in range(1, numero + 1):
        resultado *= i

    # Exibe o resultado
    print(f"{numero}! = {resultado}")
