import math

def entrada():
    global a, b, c

    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))


def calcular():
    global delta, x1, x2

    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

    elif delta == 0:
        x1 = -b / (2 * a)


def saida():
    if a == 0:
        print("Não é uma equação do 2º grau.")

    elif delta < 0:
        print("Não existem raízes reais.")

    elif delta == 0:
        print("Existe uma raiz real:")
        print("X =", x1)

    else:
        print("Existem duas raízes reais:")
        print("X1 =", x1)
        print("X2 =", x2)


def main():
    entrada()
    calcular()
    saida()

main()
