# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:24:24 2021

@author: Caroline
"""

import tarfile

archivo_tar= tarfile.open('prub.tar.gz', 'w:gz')
archivo_tar.add= ('note.json')
archivo_tar.close()