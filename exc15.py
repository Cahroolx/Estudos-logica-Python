aluguel = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodou? '))
dias = 60
km_rodado = 0.15
#primeiro vai calcuar o aluguel vezes dias, depois o valor de km com km rodado e depois somar os dois, basicamento é so multiplicação isso tudo.
total = (aluguel * dias) + (Km * km_rodado)
print(f'O total a ser pago é de R${total:.2f}')
