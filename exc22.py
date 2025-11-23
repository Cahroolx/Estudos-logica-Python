nome = input('Digite seu nome completo: ')
maiusculas = nome.upper()
minusculas = nome.lower()
letras = len(nome) - nome.count(' ')
primeiro = nome.split()[0]

#como os propios nomes ja dizem, upper deixa todas as letras maiúsculas, lower deixa todas minusculas, len conta o número de caracteres em uma string, count conta quantos espaços tem na string e split divide a string em uma lista de palavras usanndo o espaço como separador. O [0] no final pega a primeira palavra da lista gerada pelo split, que é o primeiro nome
print(f'Seu nome em maiúscula é {maiusculas}')
print(f'Seu nome em minuscula é {minusculas}')
print(f'Seu nome tem {letras} letras')
print(f'Seu primeiro nome é {primeiro} e ele tem {len(primeiro)} letras')
