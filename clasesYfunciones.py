import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def dormir():
    logging.info('Empenzado')
    time.sleep(1)
    logging.info('Finalizado')

class UnThread(threading.Thread):
    def __init__(self,seg):
        super().__init__() 
        self.name = 'threadClase'
        self.seg = seg

    def run(self):
        logging.info('Empezando')
        time.sleep(self.seg)
        logging.info('Finalizado')

logging.info('Creando thread desde una función')
threadFunc = threading.Thread(target=dormir, name='thread desde una función')

logging.info('Creando thread desde una clase')
threadObj = UnThread(1)

logging.info('Lanzando los threads')
threadFunc.start()
threadObj.start()