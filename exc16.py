# trunc é uma função da biblioteca math que serve para remover a parte decimal de um número, retornando apenas a parte inteira, tipo 6.8 vira 6
from math import trunc
valor  = float(input('Digite um valor: '))
#o trunc ficar com () significa que ele é uma função, e o valor dentro dos () é o que sera processado por essa função
print(f'O valor digitado foi {valor} e sua porção inteira é {trunc(valor)}')
