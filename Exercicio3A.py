def fatorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i

    return resultado


def main():
    n = int(input("Digite um valor inteiro: "))

    resultado = fatorial(n)

    print("Fatorial:", resultado)


main()
