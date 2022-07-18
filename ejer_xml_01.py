# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:43:52 2021

@author: Caroline
"""

from xml.dom.minidom import parse,Node

xmltree = parse('node.xml')

for node in xmltree.getElementsByTagName('pro'):
    for node_hij in node.childNodes:
        if node_hij.nodeType==Node.TEXT_NODE:
            print(node_hij.data)