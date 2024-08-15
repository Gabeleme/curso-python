''' Escreva um programa que leia dois números inteiros e 
compare-os mostrando na tela uma mensagem: 

- O primeiro valor é maior
- O segundo valor é maior
- não existe valor maior os dois são iguais '''

primeiro_num = int(input("Informe o primeiro valor inteiro: "))
segundo_num = int(input("Informe o seguno valor inteiro: "))

if primeiro_num > segundo_num:
    print("O Primeiro número é maior que o segundo")
elif segundo_num > primeiro_num: 
    print("O Segundo número é maior que o primeiro")
else:
    print("Os dois valores são iguais")

