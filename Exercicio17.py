tempo_horas = float(input("Digite o tempo de percuso (em horas): "))
velocidade_media = float(input("Digite a velocidade média (em km/h): "))

distancia = tempo_horas * velocidade_media

litros_gastos = distancia / 12

print(f"Distancia percorrida: {distancia:.2f}")
print(f"Quantidade de litros gastos: {litros_gastos:.2f}")
