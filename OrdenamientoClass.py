# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:57:28 2021

@author: guest
"""
from OrdenableAbstract import OrdenableAbstractClass;

class Ordenamiento(OrdenableAbstractClass):
    
    #https://docs.python.org/3/library/stdtypes.html#typesseq-range
    
    def burbuja(self,elementos):
        #self.imprimir(elementos)
        for i in range(0,len(elementos),1):
           # print('\nIteracion: ' , i)
            for j in range(0,len(elementos)-1,1):#(O(n))
                if(elementos[j] > elementos[j+1]):#O(1)
                    aux = elementos[j]
                    elementos[j] = elementos[j + 1]
                    elementos[j + 1] = aux
                #self.imprimir(elementos)
        #self.imprimir(elementos)
                
            
    
    def burbuja_mejorado(self,elementos):
        #self.imprimir(elementos)
        esta_ordenado = False;
        for i in range(0,len(elementos),1):
            #print("índice: " , i)
            if (not esta_ordenado):
                esta_ordenado = True
                for j in range(0,len(elementos)-i-1):
                    if(elementos[j] > elementos[j+1]):
                        esta_ordenado = False
                        aux = elementos[j]
                        elementos[j] = elementos[j + 1]
                        elementos[j + 1] = aux
                    #self.imprimir(elementos)
            else:
                #print("Sal......")
                break
            
        #self.imprimir(elementos)
    
    def seleccion(self,elementos):
        #self.imprimir(elementos)
        for i in range(0,len(elementos)):
            minimo = i
            for j in range(i+1, len(elementos),1):
                if(elementos[j] < elementos[minimo]):
                    minimo = j
            aux = elementos[i]
            elementos[i] = elementos[minimo]
            elementos[minimo] = aux
            #self.imprimir(elementos)

        
    def insercion(self,elementos):
        for i in range(0,len(elementos)):
            aux = elementos[i]
            for j in range(i-1, -1,-1):
               # print("\ni={}j={} ".format( i,j))
                #self.imprimir(elementos)
                if (elementos[j]>aux):
                    elementos[j+1] = elementos[j]
                    elementos[j] = aux

        #self.imprimir(elementos)
    
    def merge_sort(self,elementos):
        #print(elementos)
        if(len(elementos) <= 1):
            return elementos
        izq=[];
        der=[];
        indice_medio=len(elementos)//2
        for i in range(0,indice_medio):
            izq.append(elementos[i]);
        for i in range(indice_medio,len(elementos)):
            der.append(elementos[i]);
        izq=self.merge_sort(izq)
        der=self.merge_sort(der)
        return self.merge_aux(izq,der)
 
    def merge_aux(self,izq,der):
        lista =[];
        i=0;
        j=0;
        while(i < len(izq) and j < len(der)):
            if(izq[i] <= der[j]):
                lista.append(izq[i])
                i=i+1;
            else:
                lista.append(der[j])
                j=j+1;

        while(i < len(izq)):
            lista.append(izq[i])
            i=i+1;
        while(j < len(der)):
            lista.append(der[j])
            j=j+1;

        return lista
   
    def quick_sort(self,elementos):
        #self.imprimir(elementos)
        self.quick_sort_aux(elementos, 0, len(elementos)-1)
        
    def quick_sort_aux(self,elementos, left, right):
        index = self.partition(elementos, left, right)
        if (left < index-1):
            self.quick_sort_aux(elementos, left, index-1)
        if(right >= index):
            self.quick_sort_aux(elementos, index, right)
    
    def partition(self,elementos, left, right):
        i = left
        j = right
        pivot = elementos[int((left+right)/2)]
        #print('\nLeft: {} Right: {} Índice: {} Pivote: {}'.format(left,right,int((left+right)/2),pivot))
        while(i <= j):
            while(elementos[i]<pivot):
                i+=1
            while(elementos[j]>pivot):
                j-=1
           # print("\ni= {} j= {}".format(i,j))
            if(i<=j):
                tmp = elementos[i];
                elementos[i] = elementos[j];
                elementos[j] = tmp;
                i+=1
                j-=1
            
            #self.imprimir(elementos)
        
        return i
            
            
        
    
    def imprimir(self,elementos):
        print("\nValor de elementos")
        for valor in elementos:
            print(valor, end='-')