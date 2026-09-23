def entrada():
    global a, b

    a = int(input("Digite o primeiro valor inteiro: "))
    b = int(input("Digite o segundo valor inteiro: "))


def ordenar():
    global menor, maior

    if a < b:
        menor = a
        maior = b

    else:
        menor = b
        maior = a


def saida():
    print("Ordem crescente:")
    print(menor)
    print(maior)


def main():
    entrada()
    ordenar()
    saida()


main()
