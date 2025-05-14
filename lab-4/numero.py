num1 = int(input("número 1: "))
num2 = int(input("número 2: "))
num3 = int(input("número 3: "))

if num1 >= num2 and num1 >= num3:
    print(f"O maior número é {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"O maior número é {num2}")
else:
    print(f"O maior número é {num3}")