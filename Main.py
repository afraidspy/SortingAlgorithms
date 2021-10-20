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
    for i in range(1000):
        data.append(random.randint(1,10000000))
    
    return data

#data = [1,5,4,2,0,0,9]
#data = [3,7,11,2,9,1,8,5,10,6,4]
data = genera_aleatorios()
ordenamiento = Ordenamiento()
print(data)
#data = [1639672, 9080605, 7805992, 7530815, 292783, 8622560, 9751812, 8452579, 9321389, 281230, 1394183, 1483328, 3969962, 1988574, 5700117, 6189447, 4655291, 1422682, 9646675, 8670795, 7616764, 2440641, 210415, 5112990, 5347165, 5708287, 3824783, 6006026, 6903846, 749178, 9043323, 2868956, 7217003, 4004431, 1093061, 4318659, 3742505, 9092739, 4018046, 7257626, 9747026, 3019513, 518699, 7449038, 7535701, 782594, 1681710, 9182579, 7715822, 1523311, 25467, 4205725, 8068373, 4711235, 6664005, 4557819, 9557868, 7039034, 8235154, 4900164, 1593077, 7105079, 3584528, 5875968, 6193030, 9473556, 2897806, 9321419, 1786810, 8467737, 6456655, 17062, 8678988, 4433043, 2333707, 3218550, 6630543, 7161579, 8350566, 3321079, 1717451, 9360084, 5206476, 8296190, 1744200, 2411779, 7864320, 2406878, 4048925, 4121151, 8901654, 9205112, 9822295, 1336000, 1969238, 6810333, 4831283, 7845687, 5349172, 621829]
print("Burbuja normal...")
tiempo_inicio = time.time()
ordenamiento.burbuja(data);
tiempo_fin = time.time()-tiempo_inicio
print("Burbuja normal: ", tiempo_fin)
#data = [1,2,3,4,5,6]
print("Burbuja mejorado...")
ordenamiento.burbuja_mejorado(data)
#data = [7,6,2,9,3,1,8,4,5]
tiempo_inicio = time.time()
ordenamiento.seleccion(data)
tiempo_fin = time.time()-tiempo_inicio
print("Burbuja mejorado: ", tiempo_fin)
print("Insercion")
tiempo_inicio = time.time()
ordenamiento.insercion(data)
tiempo_fin = time.time()-tiempo_inicio
print("Inserción: ", tiempo_fin)
#data = [79,21,15,99,88,65,75,85,76,46,84,24]
#data = [30,50,12,15,45]
#data = ["jess","aana","pedro","salu","a"]
print("Quicksort")
tiempo_inicio = time.time()
ordenamiento.quick_sort(data)
tiempo_fin = time.time()-tiempo_inicio
print("Quicksort: ", tiempo_fin)
print("Mergesort")
tiempo_inicio = time.time()
ordenamiento.merge_sort(data)
tiempo_fin = time.time()-tiempo_inicio
print("Mergesort: ", tiempo_fin)



