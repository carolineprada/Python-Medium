# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:52:58 2021

@author: Caroline
"""
##INICIALIZADOR => Inicializar los objetos 
##Herencia simple => una clase hereda objetos a otra
##Herencia múltiple => una clase accede a los métodos y variables de otra


class Persona:
    nBrazos=0
    nPiernas=0
    cabello=True
    cCabello= "Defecto"
    hambre=0

    #Inicializador, asignar valor inicial a los objetos
    def __init__(self):
        self.nBrazos=2
        self.nPiernas=2


    #Método vacío
    def dormir():
        pass

    #Modifica Atributos
    def comer(self):
        self.hambre=9


class Hombre(Persona):
    nombre= "Defecto"
    genero= "M"
    
    #Modifica atributos y add parámetros
    def cambiNomb(self, nombre):
        self.nombre=nombre
    
    

class Mujer(Persona):
    nombre= "Defecto"
    genero= "F"
    
    
#Llamar clase, acceder a los objetos
carol=Mujer()
carol.comer()

print(carol.hambre)
    