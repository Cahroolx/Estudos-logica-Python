largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
#calculo de area da parede, largura vezes altura, e quantidade de tinta necessaria para pintar a parede, area dividido por 2 (1 litro pinta 2m²)
area = altura * largura
#2 equivale a 1 litro de tinta para cada 2 metros quadrados
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura:.0f}x{altura:.0f} e sua área é de {area}m². Para pintar essa parede, você precisará de {tinta}l de tinta.')