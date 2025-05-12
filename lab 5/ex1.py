while True:
    senha = input("Digite sua senha: ")

    numeros = ''
    caracteres = ''
    
    for i in range(len(senha)):
        if senha[i].isnumeric():
            numeros = numeros + senha[i]
        elif senha[i].isalpha():
            caracteres = caracteres + senha[i]

    if len(numeros) < 1:
        print("Sua senha precisa ter pelo menos um número. Digite novamente!")
    elif len(caracteres) < 1:
        print("Sua senha precisa ter pelo menos uma letra. Digite novamente!")
    elif " " in senha:
        print("Sua senha não pode conter espaços. Digite novamente!")
    else:
        break

print(f"Sua senha: {senha}")
print(f"Números: {numeros}")
print(f"Letras: {caracteres}")