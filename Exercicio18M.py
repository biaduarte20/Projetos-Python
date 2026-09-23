def entrada():
    global a, b

    a = int(input("Digite o primeiro valor inteiro: "))
    b = int(input("Digite o segundo valor inteiro: "))


def calcular():
    global maior, menor, diferenca

    if a > b:
        maior = a
        menor = b
    else:
        maior = a
        menor = b

    diferenca = maior - menor


def saida():
    print("A diferença do maior pelo menor é:", diferenca)


def main():
    entrada()
    calcular()
    saida()


main()

