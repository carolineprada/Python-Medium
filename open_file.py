# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:32:18 2021

@author: Caroline
"""

#Crear Archivo
#\n: Salto de línea
#W: Escritura
#A: Adiciona líneas nuevas, respeta las actuales
#R: Modo de lectura

#Crear Archivo
def crearArchivo():
    docu=open('file.txt', 'w')
    docu.close()

#Escribir Archivo
def abrirArchivo():
    docu=open('file.txt', 'a')
    docu.write('Nana\n')
    docu.write('Coffee')
    docu.close()
 
#Leer Archivo
def leerArchivo():
    docu=open('file.txt', 'r')
    line=docu.readline()
    
    while line != "":
        print(line)
        line=docu.readline()
    
    docu.close()

    
#crearArchivo()    
#abrirArchivo()
leerArchivo()
