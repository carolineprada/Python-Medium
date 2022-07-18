# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:34:38 2021

@author: Caroline
"""

def saludo(idioma):
    def saludo_es():
        print("Hola")
        
    def saludo_pg():
        print("Olá")
        
    #Función
    idioma_func={"es": saludo_es,
                 "pg": saludo_pg }
    
    return idioma_func[idioma]

saludar=saludo("pg")
saludar()