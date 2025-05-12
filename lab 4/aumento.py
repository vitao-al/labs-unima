salario = float(input("Digite o seu salário: "))

if salario < 2000:
    salario = salario + (salario * 0.10) + 200
elif salario >= 2000 <= 5000:
    salario = salario + (salario * 0.08) + 150
elif salario > 5000:
    salario = salario + (salario * 0.05)

print(f"Seu novo salário é: R${salario:.2f}")
