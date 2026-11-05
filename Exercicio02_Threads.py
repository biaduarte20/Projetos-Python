import threading
import time
import random


def somar_linha(id, valores):
    soma = 0

    for valor in valores:
        soma = soma + valor
        time.sleep(0.2)

    print("Linha #" + str(id))
    print("Valores:", valores)
    print("Resultado da soma:", soma)
    print("------------------------")


threads = []

for id in range(1, 4):

    valor1 = random.randint(1, 100)
    valor2 = random.randint(1, 100)
    valor3 = random.randint(1, 100)
    valor4 = random.randint(1, 100)
    valor5 = random.randint(1, 100)

    parametros = (id, [valor1, valor2, valor3, valor4, valor5])

    thread = threading.Thread(target=somar_linha, args=parametros)

    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()