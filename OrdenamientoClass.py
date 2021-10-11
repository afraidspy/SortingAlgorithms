# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 07:22:52 2021

@author: guest
"""
from OrdenableAbstract import OrdenableAbstractClass
class Ordenamiento(OrdenableAbstractClass):
    
    def burbuja(self,elementos):
        self.imprimir(elementos)#O(n)
        #[0,len(elementos)-1]
        for i in range(0,len(elementos),1): #O(n)
            print('\nIteracion: ' , i)
            for j in range(0,len(elementos)-1,1):#O(n)
                if(elementos[j] > elementos[j+1]): #O(1)
                    aux = elementos[j]
                    elementos[j] = elementos[j + 1]
                    elementos[j + 1] = aux
                self.imprimir(elementos)
                
        self.imprimir(elementos)
                
            
    def burbuja_mejorado(self,elementos):
        pass
    
    def seleccion(self,elementos):
        pass

    
    def insercion(self,elementos):
        pass
    
    def merge_sort(self,elementos):
        pass
    
    def quick_sort(self,elementos):
        pass
    
    def imprimir(self,elementos):
        #O(n)
        print("\nValor de elementos")
        for valor in elementos:
            print(valor, end='-')