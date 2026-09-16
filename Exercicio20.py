import math

a = float(input("Digite A: "))
b = float(input("Digite B: "))
c = float(input("Digite C: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print("Existe uma raiz real:", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print("Raiz 1:", x1)
    print("Raiz 2:", x2)
