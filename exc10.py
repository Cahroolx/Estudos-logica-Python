carteira = float(input('Quanto de dinheiro você tem na carteira? R$'))
#conversão de real para dólar, valor do real dividido pela cotação do dólar (5.34 no momento)
US = carteira / 5.34
print(f'Com R${carteira} você pode comprar US${US:.2f}')