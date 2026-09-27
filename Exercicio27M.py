def entrada():
    voltas = int(input("Digite o número de voltas: "))
    extensao = float(input("Digite a extensão do circuito (em metros): "))
    tempo = float(input("Digite o tempo de duração (minutos): "))

    return voltas, extensao, tempo


def calcular_velocidade(voltas, extensao, tempo):
    distancia = voltas * extensao
    distancia_km = distancia / 1000
    tempo_horas = tempo / 60

    velocidade = distancia_km / tempo_horas

    return velocidade


def saida(velocidade):
    print(f"Velocidade média: {velocidade:.2f} km/h")


def main():
    voltas, extensao, tempo = entrada()
    velocidade = calcular_velocidade(voltas, extensao, tempo)
    saida(velocidade)


main()
