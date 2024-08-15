cpf = '123.456.789-00' 
senha = '01020304'
saldo = 1000


print("--Bem vindo--")
inserir_cpf = str(input("Informe seu cpf contendo os traços e pontos: "))
while inserir_cpf != cpf:
    print("cpf invalido")
    inserir_cpf = str(input("Informe seu cpf novamente:"))
inserir_senha = str(input("Senha: "))
while inserir_senha != senha:
    inserir_senha = str(input("senha incorreta, informe a senha novamente: "))
print('-' * 30)
while True:
    print('Menu:\n'
        '1 - Saldo\n'
        '2 - Deposito\n'
        '3 - Saque\n'
        '0 - Sair')
    escolha = int(input("Escolha o que deseja realizar: "))

    while escolha != 0 and escolha != 1 and escolha != 2 and escolha != 3:
        escolha = int(input("valor invalido, escolha novamente: "))
    if escolha == 1:
        print(f'O saldo total da conta é de R$:{saldo:.2f}')
        print('-'* 30)
    elif escolha == 2:
        deposito = float(input("Informe o valor que deseja depositar: R$ "))
        print(f'O saldo da sua conta era de R$:{saldo}')
        print(f'Foi efetuado um deposito no valor de R$:{deposito}')
        saldo += deposito
        print(f'O valor da sua conta atual após o deposito é de R$:{saldo}')
        print('-'* 30)
    elif escolha == 3:
        print(f'O valor atual em sua conta é de R$:{saldo}')
        saque = float(input("Informe o valor do Saque: "))
        saldo -= saque
        print(f'O valor sacado foi R${saque}, saldo atual da conta é de R$:{saldo}')
    else:
        break 
print("Fim do programa")





