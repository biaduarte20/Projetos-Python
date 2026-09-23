def entrada():
    global hora_inicio, minuto_inicio
    global hora_final, minuto_final

    hora_inicio = int(input("Digite a hora de início: "))
    minuto_inicio = int(input("Digite o minuto de início: "))

    hora_final = int(input("Digite a hora de término: "))
    minuto_final = int(input("Digite o minuto de término: "))


def calcular():
    global inicio, final, duracao
    global horas, minutos

    inicio = hora_inicio * 60 + minuto_inicio
    final = hora_final * 60 + minuto_final

    if final <= inicio:
        final = final + 24 * 60

    duracao = final - inicio

    horas = duracao // 60
    minutos = duracao % 60


def saida():
    print("Duração do jogo:", horas, "hora(s) e",
          minutos, "minuto(s).")


def main():
    entrada()
    calcular()
    saida()


main()
