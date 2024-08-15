''' Insira um valor para que ele seja testado e descubra 
cada coisa que ele corresponde'''

a = input("Digite algo: ")

print("O tipo primitivo desse valor é:", type(a))
print("Só tem espaços?", a.isspace())
print("É um numero?", a.isnumeric())
print("É alfabetico?", a.isalpha())
print("É alfanumerico?", a.isalnum())
print("Está em maiusculo?", a.isupper())
print("Está em minusculo?", a.islower())
print("Está capitalizada?", a.istitle())

