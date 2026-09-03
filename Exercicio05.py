a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

delta = (b * 2) - (4 * a * c)

x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print((f"As raizes reais são: x1 = {x1} e x2 = {x2}"))