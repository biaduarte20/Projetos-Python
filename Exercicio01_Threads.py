import threading
import time


def executar_thread(id):
    time.sleep(0.5)
    print("Thread #" + str(id))


threads = []

for id in range(1, 6):
    thread = threading.Thread(target=executar_thread, args=(id,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()