def entrada():
    global numero

    numero = int(input("Digite um valor inteiro: "))


def verificar():
    global divisivel2, divisivel3

    divisivel2 = numero % 2 == 0
    divisivel3 = numero % 3 == 0


def saida():
    if divisivel2 and divisivel3:
        print("O número é divisível por 2 e por 3.")

    elif divisivel2:
        print("O número é divisível apenas por 2.")

    elif divisivel3:
        print("O número é divisível apenas por 3.")

    else:
        print("O número não é divisível por 2 nem por 3.")


def main():
    entrada()
    verificar()
    saida()


main()