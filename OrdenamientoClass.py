# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:57:28 2021

@author: guest
"""
from OrdenableAbstract import OrdenableAbstractClass;

class Ordenamiento(OrdenableAbstractClass):
    
    #https://docs.python.org/3/library/stdtypes.html#typesseq-range
    
    def burbuja(self,elementos):
        self.imprimir(elementos)
        for i in range(0,len(elementos),1):
            print('\nIteracion: ' , i)
            for j in range(0,len(elementos)-1,1):#(O(n))
                if(elementos[j] > elementos[j+1]):#O(1)
                    aux = elementos[j]
                    elementos[j] = elementos[j + 1]
                    elementos[j + 1] = aux
                self.imprimir(elementos)
        self.imprimir(elementos)
                
            
    
    def burbuja_mejorado(self,elementos):
        self.imprimir(elementos)
        esta_ordenado = False;
        for i in range(0,len(elementos),1):
            print("índice: " , i)
            if (not esta_ordenado):
                esta_ordenado = True
                for j in range(0,len(elementos)-i-1):
                    if(elementos[j] > elementos[j+1]):
                        esta_ordenado = False
                        aux = elementos[j]
                        elementos[j] = elementos[j + 1]
                        elementos[j + 1] = aux
                    self.imprimir(elementos)
            else:
                print("Sal......")
                break
            
        self.imprimir(elementos)
    
    def seleccion(self,elementos):
        self.imprimir(elementos)
        for i in range(0,len(elementos)):
            minimo = i
            for j in range(i+1, len(elementos),1):
                if(elementos[j] < elementos[minimo]):
                    minimo = j
            aux = elementos[i]
            elementos[i] = elementos[minimo]
            elementos[minimo] = aux
            self.imprimir(elementos)

        

    
    def insercion(self,elementos):
        aux=0
        for i in range(0,len(elementos)):
            aux = elementos[i]
            for j in range(i-1, -1,-1):
                self.imprimir(elementos)
                if (elementos[j]>aux):
                    elementos[j+1] = elementos[j]
                    elementos[j] = aux

        self.imprimir(elementos)
    
    def merge_sort(self,elementos):
        pass
    
    def quick_sort(self,elementos):
        pass
    
    def imprimir(self,elementos):
        #O(n)
        print("\nValor de elementos")
        for valor in elementos:
            print(valor, end='-')