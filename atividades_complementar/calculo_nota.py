# Sistema de calculo de notas 
traco_dez_vezes = '-'* 10

print(traco_dez_vezes)

print("Sistema de calculo de notas")
print("Informe o valor das suas notas")

print(traco_dez_vezes) 

Ac1 = float(input("Informe a nota da sua AC1: "))
Ac2 = float(input("Informe a nota da sua AC2: "))
Ag = float(input("Informe a nota da sua Ag: "))
Af = float(input("Informe a nota da sua Af: "))

print(traco_dez_vezes)

media = (Ac1 * 0.15) + (Ac2 * 0.30) + (Ag * 0.10) + (Af * 0.45)

if media > 5:
    print("APROVADO")
else:
    print('REPROVADO')

print(f"A sua nota final é: {media:.2f}")

