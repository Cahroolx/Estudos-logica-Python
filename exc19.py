#choise é uma função da biblioteca random que serve para selecionar um item aleatório de uma lista ou sequência.
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

#[ ] indica que é uma lista, ou seja, uma coleção de valores que podem ser acessados individualmente. nesse caso a lista contém os nomes dos quatro alunos. E uma observação começa por 0 e nao por 1. N1 equivale a 0 e assim por diante.
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O aluno escolhido foi: {escolhido}')