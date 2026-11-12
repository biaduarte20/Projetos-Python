import threading
import time
import random

QUANTIDADE_SAPOS = 5
DISTANCIA_MAXIMA = 50

semaforo_console = threading.Semaphore(1)


def mostrar(mensagem):
    semaforo_console.acquire()
    print(mensagem, flush=True)
    semaforo_console.release()


def sapo(numero):

    distancia_percorrida = 0

    mostrar(f"Sapo {numero} iniciou a corrida!")

    while distancia_percorrida < DISTANCIA_MAXIMA:

        salto_maximo = random.randint(1, 5)

        tamanho_salto = random.randint(0, salto_maximo)

        distancia_percorrida += tamanho_salto

        mostrar(
            f"Sapo {numero}: salto de {tamanho_salto} cm. "
            f"Distancia percorrida: {distancia_percorrida} cm."
        )

        time.sleep(0.2)

    mostrar(
        f"Sapo {numero} chegou! "
        f"Posicao final: {distancia_percorrida} cm."
    )


if __name__ == "__main__":

    threads = []

    for numero in range(1, QUANTIDADE_SAPOS + 1):

        thread = threading.Thread(
            target=sapo,
            args=(numero,)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Corrida encerrada!")