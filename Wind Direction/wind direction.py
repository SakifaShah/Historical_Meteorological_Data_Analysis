# -*- coding: utf-8 -*-
"""
Created on Mon May  9 13:18:19 2022

@author: Eutech
"""

import pandas as pd
import numpy as np
import datetime
import random

from datetime import datetime

input_file = "WD_sep_oct_nov_9_11.xlsx"
dataset = pd.read_excel(input_file)
#dataset = dataset.drop(labels=0, axis=0)
#print(dataset)

time = dataset.iloc[:,0]
#print(time_dict)
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}


t22_5 = [[k, random.uniform(50, 90)] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(100, 160)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(100, 240)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(200, 300)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(90, 360)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(0, 360)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
#print(all)
all_df=pd.DataFrame(all, columns=['Date', 'WD'])
print(all_df.head(15))

all_cv=all_df.to_csv('WD_sep_oct_nov_2019.csv', index=False)