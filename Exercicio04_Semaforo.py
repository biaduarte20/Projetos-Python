import threading
import time
import random

QUANTIDADE_EQUIPES = 7
CARROS_POR_EQUIPE = 2
QUANTIDADE_VOLTAS = 3

semaforo_pista = threading.Semaphore(5)

semaforos_equipes = {
    f"Equipe {letra}": threading.Semaphore(1)
    for letra in "ABCDEFG"
}

semaforo_console = threading.Semaphore(1)
semaforo_contador = threading.Semaphore(1)

carros_na_pista = 0

TEMPO_MINIMO_VOLTA = 1.0
TEMPO_MAXIMO_VOLTA = 3.0


def mostrar(mensagem):
    semaforo_console.acquire()
    print(mensagem, flush=True)
    semaforo_console.release()


def piloto(equipe, numero_carro):

    global carros_na_pista

    identificacao = f"{equipe} - Carro {numero_carro}"

    mostrar(f"{identificacao} esta aguardando para entrar na pista.")

    semaforo_equipe = semaforos_equipes[equipe]

    semaforo_equipe.acquire()

    try:

        mostrar(f"{identificacao} conseguiu a autorizacao da equipe.")

        semaforo_pista.acquire()

        try:

            semaforo_contador.acquire()
            carros_na_pista += 1
            quantidade = carros_na_pista
            semaforo_contador.release()

            mostrar(
                f"{identificacao} entrou na pista. "
                f"Carros na pista: {quantidade}/5."
            )

            for volta in range(1, QUANTIDADE_VOLTAS + 1):

                duracao_prevista = random.uniform(
                    TEMPO_MINIMO_VOLTA,
                    TEMPO_MAXIMO_VOLTA
                )

                inicio = time.perf_counter()

                time.sleep(duracao_prevista)

                tempo_volta = time.perf_counter() - inicio

                mostrar(
                    f"{identificacao} completou a volta "
                    f"{volta}/3 em {tempo_volta:.2f} segundos."
                )

            mostrar(f"{identificacao} terminou as tres voltas e saiu da pista.")

        finally:

            semaforo_contador.acquire()
            carros_na_pista -= 1
            semaforo_contador.release()

            semaforo_pista.release()

    finally:

        semaforo_equipe.release()


if __name__ == "__main__":

    threads = []

    for letra in "ABCDEFG":

        equipe = f"Equipe {letra}"

        for numero in range(1, CARROS_POR_EQUIPE + 1):

            thread = threading.Thread(
                target=piloto,
                args=(equipe, numero)
            )

            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print("Treino de Formula 1 encerrado!")
    print("Todos os pilotos completaram suas tres voltas.")