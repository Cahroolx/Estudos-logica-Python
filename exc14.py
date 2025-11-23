C = float(input('Informe a temperatura em °C: '))
#parece complicado ne? kakakak mas é simples, a coversão de Celsius para Fahrenheit é feita multiplicando a temperatura em Celsius por 9 dividido por 5 e somando 32 ao resultado. As vezes nao precisa bater muita cabeça, é so procurar a formula e aplicar
F = (C * (9/5)) + 32
#C:1.f significa que o valor de C sera mostrado com 1 casa decimal, tipo 10.0 ou 25.3 esse .3 depois da virgula é que significa a casa decimal
print(f'A temperatura de {C:.1f}°C corresponde a {F:.1f}°F')
