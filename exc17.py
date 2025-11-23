#hypot é uma função da biblioteca math que calcula a hipotenusa de um triângulo retângulo dado os comprimentos dos dois catetos
from math import hypot
CO = float(input('Comprimento do cateto oposto: '))
CA = float(input('Comprimento do cateto adjacente: '))
#calculando a hipotenusa usando a função hypot, passando os valores dos catetos como argumentos. a formula usada basicamente é: a² + b² = c², onde c é a hipotenusa
hi = hypot(CO,CA)
print(f'A hipotenusa vai medir {hi:.2f}')
