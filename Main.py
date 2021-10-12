# -*- coding: utf-8 -*-

from OrdenamientoClass import Ordenamiento

import random
import time


def genera_aleatorios():
    data = []
    for i in range(10000000):
        data.append(random.randint(1,10))
    
    return data

ordenamiento = Ordenamiento()

data = genera_aleatorios();

tiempo_inicio = time.time()
ordenamiento.burbuja(data)
tiempo_fin = time.time()

