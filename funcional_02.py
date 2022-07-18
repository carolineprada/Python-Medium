# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:13:38 2021

@author: Caroline
"""

#ejercicio2

from functools import reduce

numeros = (1,2,4,5,3,6)

def sum(x,y):
    return x+y

sumar= reduce(sum, numeros)

print(sumar)