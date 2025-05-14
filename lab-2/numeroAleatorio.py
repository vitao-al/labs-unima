'''
4) Gere um número inteiro aleatório com randint entre 1 e 100, printe-o, e
depois calcule o fatorial deste número, printando o resultado.

'''

from math import factorial
from random import randint

num = randint(1, 100)
print(f'Número aleatório gerado: {num}')

fatorial = print(f'Fatorial de {num}: {factorial(num)}')