# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:12:02 2021

@author: Caroline
"""

#Comprimir tipo GZ

import gzip

with open('prueb_zip.py', 'rb') as original:
    with gzip.open('archi.txt.gz', 'wb') as archivo:
        archivo.writelines(original)
        