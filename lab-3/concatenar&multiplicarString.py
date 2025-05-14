'''
4) Crie um programa que deve receber do usuário 2 palavras e 1 inteiro. Depois,
o programa deve fazer 3 prints:
a) O primeiro deve mostrar as palavras concatenadas.
b) O segundo deve printar uma palavra em cada linha no mesmo print.
c) O terceiro deve repetir as duas palavras o número de vezes que foi
recebido pelo inteiro que o usuário informou.

'''

print('+' + 60*'='+'+')

# entradas
palavra1 = input("Digite uma palavra: ")

palavra2 = input("Digite outra palavra: ")

num_vezes = int(input("Digite um número: "))

print('+' + 60*'='+'+')

# imprimindo as duas palavras concatenadas

print(f"Concatenação das palavras {palavra1} e {palavra2}:", f"{palavra1}" + f"{palavra2}")

print('+' + 60*'='+'+')

# imprimindo as duas palavras em cada linha

print("Imprimindo as duas palavras em cada linha")
print(palavra1, palavra2, sep="\n")

print('+' + 60*'='+'+')

# imprimindo as duas palavras repetidas

print(f"Repetindo as duas palavras {num_vezes} vezes:\n")
print(palavra1*num_vezes, palavra2*num_vezes, sep="\n")

print('+' + 60*'='+'+')