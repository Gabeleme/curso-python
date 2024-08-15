# Receber dois números e mostrar o maior deles.

n1 = int(input("Informe um valor inteiro: "))
n2 = int(input("Informe um valor inteiro: "))

if n1 > n2:
    print(f'O maior valor foi {n1}')
elif n2 > n1:
    print(f'O maior valor foi {n2}')
else: 
    print("Os dois valores são iguais")