def entrada():
    global nota1, nota2, nota3, nota4

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))


def calcular():
    global media

    media = (nota1 + nota2 + nota3 + nota4) / 4


def saida():
    print("Média:", media)

    if media >= 6.0:
        print("APROVADO")

    elif media >= 3.0:
        print("EXAME")

    else:
        print("RETIDO")


def main():
    entrada()
    calcular()
    saida()


main()
