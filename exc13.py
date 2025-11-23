salario = float(input("Digite o seu salário: R$:"))
#calcula o aumento de 15% no salário, salario vezes 0.15(15 dividido por 100)
aumento = salario * 0.15
#novo salário, salario mais o valor do aumento
salario_final = salario + aumento
print(f'Seu novo salário com o aumento de 15% é de R${salario_final:.2f}')