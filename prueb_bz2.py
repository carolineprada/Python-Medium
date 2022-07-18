# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:16:03 2021

@author: Caroline
"""

import bz2

cadena= b"Cadena, cadena  tu"
cadena_c=bz2.compress(cadena)

print(cadena_c)