import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


cantidad = 1
lock = threading.Lock()

def sumarUno():
    logging.info("sumar")
    global cantidad
    global lock
    lock.acquire()
    cantidad += 1
    lock.release()
    logging.info("finalizar")

def multiplicarPorDos():
    logging.info("multiplicar")
    global cantidad
    global lock
    lock.acquire()
    try:
        cantidad *= 2
    finally:
        lock.release()
        logging.info("finalizar")

    






threadSumarUno = threading.Thread(target=sumarUno, name='multiplicar')
threadMultiplicarPorDos = threading.Thread(target=multiplicarPorDos, name = 'sumar' )

threadMultiplicarPorDos.start()

lock.acquire()
threadSumarUno.start()




threadMultiplicarPorDos.join()
threadSumarUno.join()


print(cantidad)


    