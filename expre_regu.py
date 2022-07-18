# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:18:04 2021

@author: Caroline
"""

import re

patron=re.compile("\d\d\d")

print(re.search(r"k", "kristofer"))
print(re.search(r"\d\d\d", "Car158ol"))
print(patron.search("Kilo348").group())

if(re.search("\Aa[0-9].*(end|fin)$", "a58 dsds5d fin")):
    print("Se encontró el patrón")
    
    
print(re.sub(r"\d", "*", "Carol102589"))    
    

regex = re.compile(r"ab", re.IGNORECASE)
print(regex.search("Juan Abellaneda"))