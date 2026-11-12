import threading
import time
import random

DISTANCIA_CORREDOR = 200

semaforo_porta = threading.Semaphore(1)
semaforo_console = threading.Semaphore(1)


def mostrar(mensagem):
    semaforo_console.acquire()
    print(mensagem, flush=True)
    semaforo_console.release()


def pessoa(numero):

    velocidade = random.uniform(4.0, 6.0)

    tempo_caminhada = DISTANCIA_CORREDOR / velocidade

    mostrar(
        f"Pessoa {numero} comecou a caminhar. "
        f"Velocidade: {velocidade:.2f} m/s."
    )

    time.sleep(tempo_caminhada)

    mostrar(f"Pessoa {numero} chegou a porta e esta aguardando.")

    semaforo_porta.acquire()

    try:
        tempo_porta = random.uniform(1.0, 2.0)

        mostrar(
            f"Pessoa {numero} esta abrindo e atravessando "
            f"a porta. Tempo: {tempo_porta:.2f} segundos."
        )

        time.sleep(tempo_porta)

        mostrar(f"Pessoa {numero} atravessou a porta.")

    finally:
        semaforo_porta.release()


if __name__ == "__main__":

    threads = []

    for numero in range(1, 5):

        thread = threading.Thread(
            target=pessoa,
            args=(numero,)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Todas as pessoas atravessaram a porta!")