''' Crie um programa que leia dois valores e mostre um menu
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa 

Seu programa deverá realizar a operação solicitada 
em cada caso 
'''

num1 = int(input("Informe um valor inteiro: "))
num2 = int(input("Informe um valor inteiro: "))

escolha = 0
while escolha != 5:
    print("------------------------")
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair do programa")
    escolha = int(input("Escolha uma opção: "))
    print("------------------------")

    if escolha == 1:
        soma = num1 + num2
        print(f"A soma dos valores {num1} + {num2} tem como resultado {soma}")
    elif escolha == 2: 
        mult = num1 * num2
        print(f"A multiplicação entre {num1} * {num2} tem como resultado {mult}")
    elif escolha == 3:
        if num1 > num2:
            maior = num1
            print(f"entre {num1} e {num2} o maior valor é {maior}")
        elif num2 > num1:
            meior = num2
            print(f"entre {num1} e {num2} o maior valor é {maior}")
        else:
            print("Os dois valores são iguais")
        
    elif escolha == 4:
        print("Informe novos valores")
        num1 = int(input("Informe um valor inteiro: "))
        num2 = int(input("Informe um valor inteiro: "))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente!')
print('Fim do Programa!')
