frase = input('Digite uma frase: ').strip() #strip remove espaços desnecesários no começo e final da string
a = frase.lower().count('a')
#isso aqui foi meio complicado pra eu compreender, mas basicamente o lower() converte toda a frase para minúscula, garantindo que a contagem de 'a' seja precisa, independentemente de serem maiúsculas ou minúsculas, o count('a') conta quantas vezes a letra 'a' aparece na frase
print(f'A letra "a" aparece {a} vezes na frase.')
posicao = frase.lower().find('a')  #find procura a primeira ocorrência da letra 'a' na frase, retornando a posição dela
print(f'A primeira letra "a" apareceu na posição {posicao + 1}.')
posicao_ultima = frase.lower().rfind('a')  # rfind procura da direita para a esquerda
print(f'A última letra "a" apareceu na posição {posicao_ultima + 1}.') #voce pode ficar confuso com as posições, ja que a contagem começa do 0, ou seja, a primeira letra da frase está nessa posição.   
#por isso somei +1 para ajustar a contagem e mostrar a posição correta para o usuário.


#engraçado que esse codigo eu fiz a mó tempo e to revendo agr, simplesmente entendi as coisas mas vendo hoje(pq no tempo eu dei uma parada) eu nao entendi como cheguei a essa conclusão, mas enfim, o importante é que deu certo :P
#so mudei add o strip() e os +1 nas posições, o resto foi o eu do passado

