'''
 Crie um programa que deve receber 6 números e depois gerar uma lista em ordem crescente destes números. 

'''

num = []
lista_ordenada = []
for i in range(1, 7):
    n = int(input("digite o número: "))
    num.append(n)

for i in range(0, len(num)):
    print()