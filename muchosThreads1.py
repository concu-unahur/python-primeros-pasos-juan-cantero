import threading
import time
import logging
from clasesYfunciones import *
from tiempo import Contador


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)



contador = Contador()

contador.iniciar()
for i in range(10):
    #crear un thead
    #lanzarlo
    t1 = UnThread(0)
    t1.start()
    t1.join()
    
contador.finalizar()
contador.imprimir()