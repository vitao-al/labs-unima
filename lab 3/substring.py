# entradas
palavra = input("Digite qualquer palavra aqui:\n")
inteiro1 = int(input("Digite um número:\n"))
inteiro2 = int(input("Digite outro número:\n"))

# quebrando a string em intervalos determinados e salvando em uma variável
substring = palavra[inteiro1 - 1 : inteiro2]

# imprimindo a substring
print(f"A substring que foi extraída da palavra {palavra} foi: {substring}.")