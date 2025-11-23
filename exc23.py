num = int(input('Digite um número: '))
unidade = num // 1 % 10 # Pega o resto da divisão por 1, ou seja, o último dígito
dezena = num // 10 % 10 # Pega o resto da divisão por 10, ou seja, o penúltimo dígito
centena = num // 100 % 10 # Pega o resto da divisão por 100, ou seja, o antepenúltimo dígito
milhar = num // 1000 % 10 # Pega o resto da divisão por 1000, ou seja, o quarto último dígito

#por que dividir e depois pegar o resto? porque assim conseguimos isolar cada dígito do número, independentemente de quantos dígitos ele tenha no total, mas como isso funciona? quando dividido por 1 o número permanece o mesmo, então o resto da divisão por 1 é o último dígito. Quando dividido por 10, o último dígito é removido, então o resto da divisão por 10 do resultado é o penúltimo dígito, e assim por diante. 

#pra que serve o %10? o operador % é o chamado Modulo, que retorna o resto da divisão. Ao usar %10 estamos pegando o último dígito do número resultante da divisão inteira, assim isolando o dígito desejado.

print(f'Número {num}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')