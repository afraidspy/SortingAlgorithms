# -*- coding: utf-8 -*-

from OrdenamientoClass import Ordenamiento

import random

def genera_aleatorios():
    data = []
    for i in range(10):
        data.append(random.randint(1,10))
    
    return data

ordenamiento = Ordenamiento()

data = genera_aleatorios();

ordenamiento.burbuja(data)
