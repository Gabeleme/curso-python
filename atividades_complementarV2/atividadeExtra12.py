''' Receber numerador e denominador. Calcular e mostrar o resultado da 
divisão, desde que possível (denominador diferente de zero). Se não for 
possível dividir, apenas escreva “não existe divisão por zero” '''

numerador = float(input("Informe o numerador: "))
denominador = int(input("Informe o denominador: "))

if denominador != 0:
    resultado = numerador // denominador
    print(f"O resultado da divisão entre {numerador} e {denominador} é {resultado}")
else:
    print("Não é possivel realizar a divisão pois o número informado foi 0")