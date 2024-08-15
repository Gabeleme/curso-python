larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt
print("Sua parede tem a dimensão de {}X{} e sua área é de {}".format(larg, alt, area))
tinta = area /2 
print("Para pintar essa parede, você precisará de {}L de tinta".format(tinta))