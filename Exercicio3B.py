def fatorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i

    return resultado


def dividir(a, b):
    resultado = a / b

    return resultado


def main():
    n = int(input("Digite o valor de N: "))

    soma = 1

    for i in range(1, n + 1):
        fat = fatorial(i)
        parcela = dividir(1, fat)
        soma = soma + parcela

    print("Resultado:", soma)


main()
