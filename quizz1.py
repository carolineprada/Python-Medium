# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:18:28 2021

@author: Caroline
"""
#Nota: con el ordenamiento sólo se hace una copia aplicando el comando
#sorted= ordenar
#reverse= ordenar desc
#variable+.+sort => se aplica a la variable el cambio

lista= [3,9,6,4,10,25,32,8,7]
letra= ["ZA", "AA", "BC", "ZH", "ZE", "BS", "ND", "HD"]


print(lista)
print(sorted(lista))
print(sorted(lista, reverse=True))
lista.sort()
print(lista)

print(sorted(letra))
letra.sort()
print(letra)