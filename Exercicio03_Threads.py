import threading
import time
import random


DISTANCIA_MAXIMA = 30


def corrida(id_sapo):

    distancia = 0

    salto_maximo = random.randint(1, 5)

    print("Sapo #" + str(id_sapo) + " começou a corrida!")
    print("Tamanho máximo do pulo:", salto_maximo, "cm")
    print("------------------------")

    while distancia < DISTANCIA_MAXIMA:

        salto = random.randint(0, salto_maximo)

        if distancia + salto > DISTANCIA_MAXIMA:
            salto = DISTANCIA_MAXIMA - distancia

        distancia = distancia + salto

        print(
            "Sapo #" + str(id_sapo) +
            " pulou " + str(salto) + " cm. " +
            "Distância percorrida: " + str(distancia) +
            "/" + str(DISTANCIA_MAXIMA) + " cm."
        )

        if distancia >= DISTANCIA_MAXIMA:
            print("Sapo #" + str(id_sapo) + " CHEGOU!")
            print("------------------------")
            break

        time.sleep(0.2)


threads = []

for id_sapo in range(1, 6):

    thread = threading.Thread(target=corrida, args=(id_sapo,))

    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("A corrida terminou!")