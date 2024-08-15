''' Calcular a média de um aluno em um semestre com duas provas, onde M 
= (P1 + P2) / 2. Se a média for maior ou igual a 5 escreva “aprovado”, 
senão calcule e mostre quanto faltou para atingir 5 '''

print("--Calculo de nota--")
p1 = float(input("Informe sua nota da primeira prova: "))
p2 = float(input("Informe sua nota da segunda prova: "))

media = (p1 + p2) / 2 
falta = 5 - media 
print(f'Sua média final foi de {media:.2f}')
if media >= 5:
    print('Aprovado, uhulll')
else:
    print(f'Reprovado, faltou {falta} para que vc fosse aprovado :( ')

