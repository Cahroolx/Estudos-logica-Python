nome =input('Digite seu nome completo: ')
separação = nome.split() #split divide a string em uma lista de palavras usando o espaço como separador
print(f'Seu nome separado é: {separação}')
print(f'Seu primeiro nome é: {separação[0]}')# o [0] ´pega a primeira palavra da lista
print(f'Seu último nome é: {separação[-1]}') # -1 pega o último elemento da lista, mas por que -1? porque a contagem começa do 0, então o -1 indica o último elemento da lista, ja que se voce colcoar 1 ele vai pegar o segundo e nao realmente o ultimo :D