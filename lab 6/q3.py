'''
Crie um programa que deve ter duas listas pré-estabelecidas, uma com inteiros e outra com strings das quais todas são números. O programa deve então comparar as listas e gerar uma nova lista apenas com os números que aparecem em ambas as listas. 

'''

lista_1 = [1, 2, 3, 4, 5]
lista_2 = ['1','7','2','8', '4']
lista3 = []
for n in lista_1:
    l = chr(n + 48)
    if l in lista_2:
        lista3.append(l)
        
print(f"Saída: {lista3}")