#shuffle é uma função da biblioteca random que serve para embaralhar os elementos de uma lista de forma aleatória.
from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]
shuffle(lista)
#exibe a lista de forma embaralhada
print('A ordem de apresentação será:')
print(lista)