# refaça o exercicio de tabuada anterior so que agora usando laço for 

num = int(input("Informe o valor: "))
for c in range(1, 11):
    print('{} X {} = {}'.format(num, c, num*c))
