# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 18:36:18 2021

@author: guest
"""
import random
import time
from OrdenamientoClass import Ordenamiento

def genera_aleatorios():
    data = []
    for i in range(10):
        data.append(random.randint(1,10000000))
    
    return data

#data = [1,5,4,2,0,0,9]
data = [3,7,11,2,9,1,8,5,10,6,4]
#data = genera_aleatorios()
ordenamiento = Ordenamiento()

#print("Burbuja normal...")
#ordenamiento.burbuja(data);

#data = [1,2,3,4,5,6]

##print("Burbuja mejorado...")
#ordenamiento.burbuja_mejorado(data)
#print("Selección...")
data = [7,6,2,9,3,1,8,4,5]
#ordenamiento.seleccion(data)
#print("Insercion")
#ordenamiento.insercion(data)
data = [79,21,15,99,88,65,75,85,76,46,84,24]
#data = [30,50,12,15,45]
#data = ["jess","aana","pedro"]
ordenamiento.quick_sort(data)


