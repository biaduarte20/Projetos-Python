a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

if maior % menor == 0:
    print("O maior número é múltiplo do menor.")
else:
    print("O maior número não é múltiplo do menor.")
