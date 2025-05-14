'''
Crie um programa em que você deve receber as notas de 5 alunos de uma 
turma e imprimir ao final apenas as notas que estiverem acima (ou igual)
 à média da turma. 

'''
soma = 0
notas = []
notas1 = []
for i in range(1,6):
    print('+' + 60*'='+'+')
    nota = float(input(f"Digite a nota do {i}° aluno:"))
    notas.append(nota)
    soma += nota

media = soma / len(notas)

for nota in notas: 
    if nota >= media:
        notas1.append(nota)
print(f"A média dos 5 alunos foi {media}, e as notas igual ou acima da média são: {notas1}.")
           


