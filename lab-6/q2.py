'''
Crie um programa que deve quebrar uma lista em várias sublistas a cada enésimo valor. O valor de N deve ser recebido pelo usuário, a lista original pode ser pré-estabelecida e deve contar ao menos 10 valores. 

'''

print('+' + 60*'='+'+')
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Digite o valor de N: "))
sublistas = []

for i in range(0, len(lista_original), n):
    linha = lista_original[i:i + n]
    sublistas.append(linha)
    
print('+' + 60*'='+'+')
print(f"Sublistas: {sublistas}")

