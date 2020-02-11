import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


cantidad = 1
lock = threading.Semaphore(0)

def sumarUno():
    logging.info("sumar")
    global cantidad
    global lock
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

    






threadSumarUno = threading.Thread(target=sumarUno, name='sumar')
threadMultiplicarPorDos = threading.Thread(target=multiplicarPorDos, name = 'multiplicar' )





threadMultiplicarPorDos.start()
threadSumarUno.start()




threadMultiplicarPorDos.join()
threadSumarUno.join()


print(cantidad)


    