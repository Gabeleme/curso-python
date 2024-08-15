print('Informando os valores')
print('Para parar informe um valor negativo, lembrando que 0 não é considerado negativo')

soma = 0 
while True:
    numero = int(input('Informe um valor: '))

    if numero < 0:
        break

    soma += numero
    

print(f'A soma dos valores positivos foi de {soma}')
print('Parando o programa')