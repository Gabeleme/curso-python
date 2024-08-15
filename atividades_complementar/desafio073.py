''' Crie uma tupla preenchida com os 20 primeiros colocados
da tabela do campeonato brasileiro de futebol, na ordem
de colocação. depois mostre: 

- Apenas os 5 primeirps colocados
- Os últimos 4 colocados da tabela
- Uma lista com os times em ordem alfabetica
- Em que posição na tabela está o time do São Paulo

'''

tabela = ('Flamengo', 'Botafogo', 'Palmeiras', 'Bahia', 
          'São Paulo', 'Cruzeiro', 'Athletico Paranaense', 
          'Fortaleza', 'Bragantino', 'Vasco','Internacional', 
          'Juventude', 'Atlético-MG', 'Criciúma', 'Vitória',
          'Cuiabá', 'Corinthians', 'Grêmio', 
          'Atlético-GO', 'Fluminense',)

print("-" *15)
print(f"Os times são: {tabela}")
print("-" *15)
print(f"Os 5 primeiros colocados são: {tabela[0:5]}")
print("-" *15)
print(f"Os 4 últimos colocados são: {tabela[-4:]}")
print("-" *15)
print(f"A lista dos times em ordem alfabetica vai ficar: {sorted(tabela)}")
print("-" *15)
print(f"O time do São Paulo está em {tabela.index("São Paulo")} posição na tabela")
print("-" *15) 