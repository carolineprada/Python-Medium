# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:56:58 2021

@author: Caroline
"""

#Funciones de Python
#find= Buscar una letra en una cadena
#replace= Reemplaza datos
#strip= Eliminar los espacios
#lstrip= Elimina espacios a la izq.
#rstrip= Elimina espacios a la der.
#upper= Convierte en Mayúscula
#lower= Convierte en MMinúscula
#split= genera un separador en la cadena


cadena= " Cofee Prada"
nuevo= cadena.replace("Cofee", "Coffee")
nueva= nuevo.strip()
nueve= cadena.lstrip()
nuevi= cadena.rstrip()
mayu= nueva.upper()
minu= nueva.lower()
prueba= "Juan Camilo ? Pedro José ? Carlos Mario ? Andrés Felipe ? José Daniel"


print(cadena.find("e"))
print(cadena)
print(nueva)
print(mayu)
print(minu)
print(prueba.split("?"))
