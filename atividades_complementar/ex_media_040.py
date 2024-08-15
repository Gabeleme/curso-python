''' crie um programa que leia duas notas de um aluno e calcule
sua média, mostrando uma mensagem no final, de acordo com a média atingida: 

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9 RECUPERAÇÃO
- Média 7.0 ou superior APROVADO
'''

n1 = float(input("Informe sua primeira nota: "))
n2 = float(input("Informe sua segunda nota: "))

media = (n1 + n2) / 2 

if media >= 7:
    print("APROVADO, sua média foi {:.2f}".format(media))
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO, sua média foi {:.2f}".format(media))
else:
    print("REPROVADO, sua média foi {:.2f}".format(media))
