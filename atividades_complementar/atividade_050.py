''' desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. 
se o valor digitado for impar, desconsidere-o '''

soma = 0 
cont =0 
for n in range(1, 7):
   num = int(input('Digite um número:'))
   if num % 2 == 0:
      soma += num
      cont += 1
print('Você informou {} números pares e a soma foi {} '.format(cont, soma))
   