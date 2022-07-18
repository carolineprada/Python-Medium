# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:04:13 2021

@author: Caroline
"""
#Comprimir archivos en .zip
import zipfile

from zipfile import ZipFile

with zipfile.ZipFile('prueba.zip', 'w') as fzip:
    fzip.write('archi_json.py')
    fzip.write('note.json')
    
#Descomprimir
#fzip.extractall()    