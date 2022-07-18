# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:53:40 2021

@author: Caroline
"""

import json

with open('note.json') as file:
    data = json.load(file)
    
print(data)
print(data['clientesA'])