preco = float(input("Digite o preço do produto: R$"))
#calculo de desconto de 5% no preço do produto, preco vezes 0.05(basicamente 5 dividido por 100)
desconto = preco  * 0.05
#depois do desconto, subtrai o valor do desconto do preço original
final = preco - desconto
print(f'Agora o novo valor é de R${final:.2f} com o desconto de R${desconto:.2f}')
