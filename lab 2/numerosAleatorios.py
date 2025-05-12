'''
3) Gere 2 números reais (float) aleatórios entre 0.0 e 1.0, printe-os, depois
utilizando as funções de piso e teto, converta um número para seu piso e o
outro para seu teto (ceil e floor) e printe os valores convertidos.

'''
import random as r

from math import floor, ceil

A = r.random()
B = r.random()

print(f'Valor A entre 0 e 1 gerado aleatóriamente: {A}')
print(f'Valor B entre 0 e 1 gerado aleatóriamente: {B}')

print('+' + 60*'='+'+')

print(f'Convertendo o valor de {A} para seu piso:{floor(A)}')
print(f'Convertendo o valor de {B} para seu teto:{ceil(B)}')

print('+' + 60*'='+'+')