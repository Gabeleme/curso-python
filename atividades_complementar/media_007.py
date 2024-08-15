''' Peça para o usuario informar duas notas e faça a media delas'''

primeira = float(input("Informe a primeira nota:"))
segunda = float(input("informe a segunda nota:"))

media = (primeira + segunda) / 2 

print("A média entre {} e {} é igual a {}".format(primeira, segunda, media))