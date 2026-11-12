import threading
import time

semaforo_cruzamento = threading.Semaphore(1)
semaforo_console = threading.Semaphore(1)

sentido = ""


def mostrar(mensagem):
    semaforo_console.acquire()
    print(mensagem, flush=True)
    semaforo_console.release()


def controlar_carro(numero, origem, destino, atraso):
    global sentido

    time.sleep(atraso)

    mostrar(f"Carro {numero} chegou ao cruzamento.")

    semaforo_cruzamento.acquire()

    try:
        sentido = origem + " -> " + destino

        mostrar(f"Carro {numero} esta passando no sentido: {sentido}")

        time.sleep(2)

        mostrar(f"Carro {numero} saiu do cruzamento.")

    finally:
        semaforo_cruzamento.release()


if __name__ == "__main__":

    carros = [
        (1, "Norte", "Sul", 0.0),
        (2, "Sul", "Norte", 0.2),
        (3, "Leste", "Oeste", 0.4),
        (4, "Oeste", "Leste", 0.6)
    ]

    threads = []

    for dados in carros:
        thread = threading.Thread(
            target=controlar_carro,
            args=dados
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Todos os carros passaram pelo cruzamento!")