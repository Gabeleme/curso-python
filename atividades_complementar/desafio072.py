''' Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem extensa de zero até vinte

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso

'''

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 2:
        break
    print("Tente novamente")
print(f"Você digitou o número {cont[num]}")
