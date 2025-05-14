l1 = [1,2,3,4]
l2 = [2,4]
diferenca = []

for n in l1:
    if n not in l2:
        diferenca.append(n)

print(f"Diferença {diferenca}")