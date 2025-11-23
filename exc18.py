#radians, sin, cos, tan são funções da biblioteca math que servem para converter graus em radianos e calcular o seno, cosseno e tangente de um ângulo respectivamente.
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
#Converte o ângulo para radianos ja que o número original está em graus e o python trabalha com radianos, radianos são a medida padrão de ângulos utilizada em matemática.
seno = sin(radians(angulo)) 
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")