# -*- coding: utf-8 -*-

"""
 Clase abstracta para implementar diferentes tipos de ordenamientos
 con números reales
 Los números se ordenarán de MENOR A MAYOR
 Objetivo: Analizar su implementación y complejidad.
 @author Jess
 @version 1.0
"""
from abc import ABC, abstractmethod

class OrdenableAbstractClass:
    @abstractmethod
    def burbuja(elementos):
        """
        Ordenamiento burbuja
        Parameters
        ----------
        elementos : []float -Recibe una lista de números reales
        Returns
        -------
        []float - regresa el arreglo ordenado usado el algoritmo burbuja
        """
        pass
    @abstractmethod
    def burbuja_mejorado(elementos):
        """
        Ordenamiento burbuja mejorado
        Parameters
        ----------
        elementos : []float -Recibe una lista de números reales
        Returns
        -------
        []float - regresa el arreglo ordenado usado el algoritmo burbuja mejorado

        """
        pass
    @abstractmethod
    def seleccion(elementos):
        """
        Ordenamiento burbuja mejorado
        Parameters
        ----------
        elementos : []float -Recibe una lista de números reales
        Returns
        -------
        []float - regresa el arreglo ordenado usado el algoritmo burbuja mejorado

        """
        pass
    @abstractmethod
    def insercion(elementos):
        """
        Ordenamiento burbuja mejorado
        Parameters
        ----------
        elementos : []float -Recibe una lista de números reales
        Returns
        -------
        []float - regresa el arreglo ordenado usado el algoritmo burbuja mejorado

        """
        pass
    @abstractmethod
    def merge_sort(elementos):
        """
        Ordenamiento burbuja mejorado
        Parameters
        ----------
        elementos : []float -Recibe una lista de números reales
        Returns
        -------
        []float - regresa el arreglo ordenado usado el algoritmo burbuja mejorado

        """
        pass
    @abstractmethod
    def quick_sort(elementos):
        """
        Ordenamiento burbuja mejorado
        Parameters
        ----------
        elementos : []float -Recibe una lista de números reales
        Returns
        -------
        []float - regresa el arreglo ordenado usado el algoritmo burbuja mejorado

        """
        pass
    @abstractmethod
    def imprimir(elementos):
        """
        Ordenamiento burbuja mejorado
        Parameters
        ----------
        elementos : []float -Recibe una lista de números reales
        Returns
        -------
        []float - regresa el arreglo ordenado usado el algoritmo burbuja mejorado

        """
        pass