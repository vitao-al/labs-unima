import random

numero = random.randint(1, 10)

while True:

    numerousuario = int(input("Digite o número: "))

    if numerousuario < 1 or numerousuario > 9:
        print("Número inválido. Digite um número de 1 a 9.")
    else:
        if numerousuario == numero:
            print("Você acertou!")
            break
        elif numerousuario != numero:
            print(f"Você errou! O número correto era {numero}")
            break