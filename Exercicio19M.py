def entrada():
    global a, b

    a = float(input("Digite o primeiro valor real: "))
    b = float(input("Digite o segundo valor real: "))


def calcular():
    global maior

    if a > b:
        maior = a
    else:
        maior = b


def saida():
    print("O maior valor é:", maior)


def main():
    entrada()
    calcular()
    saida()


main()
