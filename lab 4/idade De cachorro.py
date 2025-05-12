
idade_humana = float(input("Digite a idade do cachorro em anos humanos: "))
if idade_humana <= 0:
    idade_canina = 0
elif idade_humana <= 2:
    idade_canina = idade_humana * 10.5
else:
     idade_canina = 21 + (idade_humana - 2) * 4  # 21 = 2 * 10.5
     print(f"Um cachorro com {idade_humana} anos humanos tem aproximadamente {idade_canina} anos caninos.")