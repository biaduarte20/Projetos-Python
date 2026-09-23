def entrada():
    global a, b

    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))


def verificar():
    global maior, menor, multiplo

    if a > b:
        maior = a
        menor = b

    else:
        maior = b
        menor = a

    if maior % menor == 0:
        multiplo = True

    else:
        multiplo = False


def saida():
    if multiplo:
        print("O maior número é múltiplo do menor.")

    else:
        print("O maior número não é múltiplo do menor.")


def main():
    entrada()
    verificar()
    saida()


main()

