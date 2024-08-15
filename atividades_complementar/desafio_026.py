''' faça um programa que leia uma frase pelo teclado e mostre: 
- Quantas vezes apareceu a letra A
- Em que posição ela aparece na primeira vez
- Em que posição ela aparece na ultima vez '''

frase = str(input("informe a frase: ")).upper().strip()
print("A letra 'A' apareceu {}".format(frase.count('A')))
print ('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))