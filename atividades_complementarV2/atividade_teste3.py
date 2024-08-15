def criar_saudacao(saudacao): 
		def saudar(nome):
				return f'{saudacao}, {nome}'
		return saudar 
		

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa Noite')

print(s1('LUIZ'))
print(s2('MARIA'))
print(s2('GABRIELA'))