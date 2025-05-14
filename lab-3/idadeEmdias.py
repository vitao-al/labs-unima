'''
2) Crie um programa que deve receber do usuário sua idade completa em anos,
meses e dias e deve convertê-la para seu valor total em dias e imprimí-lo
para o usuário (Ex: 28 anos, 6 meses e 11 dias = 10411 dias). Considere
todos os anos com 365 dias e todos os meses com 30 dias. Utilize apenas
números inteiros.

'''
print("Digite sua idade em anos, meses e dias!")

# Entradas
anos = int(input("Anos:\n"))
meses = int(input("Meses:\n"))
dias = int(input("Dias:\n"))

# Calcula o total de dias
total_dias = (anos * 365) + (meses * 30) + dias

# Exibe o resultado
print(f"Sua idade é: {anos} anos, {meses} meses e {dias} dias. Total de dias vivos: {total_dias}")
