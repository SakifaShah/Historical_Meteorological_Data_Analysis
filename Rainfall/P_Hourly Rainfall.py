# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 22:26:49 2022

@author: HP
"""

import pandas as pd
import numpy as np

#input file 
input_file = "Updated Mymensingh.xlsx"
dataset = pd.read_excel(input_file)
#print(dataset)

l = []
l.extend([0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.3] for i in range(334))

s = [i for n in l for i in n]
s.append(0.3)


dataset['P'] = s

print(s)
#print(len(s))
print(dataset)

dataset = dataset.to_excel("P_Mymensingh.xlsx",index=False)
