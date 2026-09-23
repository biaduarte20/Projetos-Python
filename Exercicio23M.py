def entrada():
    global a, b, c, d

    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    d = int(input("Digite o quarto valor: "))


def ordenar():
    global pos1, pos2, pos3, pos4

    numeros = [a, b, c, d]
    numeros.sort()

    pos1 = numeros[0]
    pos2 = numeros[1]
    pos3 = numeros[2]
    pos4 = numeros[3]


def saida():
    print("Ordem crescente:")
    print(pos1)
    print(pos2)
    print(pos3)
    print(pos4)


def main():
    entrada()
    ordenar()
    saida()


main()
