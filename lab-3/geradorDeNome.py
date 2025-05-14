print('+' + 60*'='+'+')
# Solicita os nomes dos pais
pai = input("Digite o primeiro nome do pai: ")
mae = input("Digite o primeiro nome da mãe: ")

print('+' + 60*'='+'+')

# calcula os pontos de corte para dividir os nomes ao meio
metade_pai = len(pai) // 2
metade_mae = len(mae) // 2

# gera o nome do filho(a) concatenando a primeira metade do nome do pai com a segunda metade do nome da mãe
nome_filho = pai[:metade_pai] + mae[metade_mae:]

# nome do filho
print(f"Nome sugerido para o filho(a): {nome_filho}")

print('+' + 60*'='+'+')
