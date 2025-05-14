"""1) Assumindo pi = 3.14, faça um programa para converter graus em radianos. A
fórmula matemática para tal conversão é:
                 Radianos = Graus / 180 X pi
Faça com que seu programa printe (usando o comando print) o valor em
radianos de 30o, 60o, 90o e 180o.
"""
pi = 3.14

radiano30 = print((30/180)*pi) # radiano de 30°
radiano60 = print((60/180)*pi) # radiano de 60°
radiano90 = print((90/180)*pi) # radiano de 90°
radiano180 = print((180/180)*pi) # radiano de 180°

# radiano de qualquer grau
radianos = print((int(input("digite o valor do grau:"))/180)*pi)