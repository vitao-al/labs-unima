'''
2) Refaça o programa que calcule a distância entre dois pontos e printe o
resultado. Porém desta vez utilize as funções de raíz quadrada e de potência.
Resolva para os casos: (1, 1) e (3, 4); (0, 0) e (10, 10); (2, 7) e (20, 30).

'''

import math as m
Xa = 1
Xb = 3

Ya = 1
Yb = 4

D = m.sqrt(m.pow(Xb - Xa,2) + m.pow(Yb - Ya,2)) # Distância entre os pontos (1,1) e (3,4)
print(f'Valor da distância entre os pontos ({Xa},{Ya}) e ({Xb},{Yb}) é: {m.ceil(D)}')

print('+' + 90*'='+'+')

Xa = 0
Xb = 10

Ya = 0
Yb = 10

D = m.sqrt(m.pow(Xb - Xa,2) + m.pow(Yb - Ya,2)) # Distância entre os pontos (0,0) e (10,10)
print(f'Valor da distância entre os pontos ({Xa},{Ya}) e ({Xb},{Yb}) é: {m.ceil(D)}')

print('+' + 90*'='+'+')

Xa = 2
Xb = 20

Ya = 7
Yb = 30

D = m.sqrt(m.pow(Xb - Xa,2) + m.pow(Yb - Ya,2)) # Distância entre os pontos (2,7) e (20,30)
print(f'Valor da distância entre os pontos ({Xa},{Ya}) e ({Xb},{Yb}) é: {m.ceil(D)}')

print('+' + 90*'='+'+')