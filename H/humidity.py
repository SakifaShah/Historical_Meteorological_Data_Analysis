# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:50:11 2022

@author: Eutech
"""
import pandas as pd
import numpy as np
import datetime
import random

from datetime import datetime

input_file = "SH_dec_jan_feb_12_2.xlsx"
dataset = pd.read_excel(input_file)
#dataset = dataset.drop(labels=0, axis=0)
#print(dataset)

time = dataset.iloc[:,0]
#print(time_dict)
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}


t22_5 = [[k, random.uniform(500, 800)] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(1000, 1200)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(1100, 1200)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(1400, 800)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(1300, 1500)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(900, 1100)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
#print(all)
all_df=pd.DataFrame(all, columns=['Date', 'H'])
print(all_df.head(15))

all_cv=all_df.to_csv('H_dec_jan_feb_2011.csv', index=False)

input_file = "SH_mar_apr_may_3_5.xlsx"
dataset = pd.read_excel(input_file)
#dataset = dataset.drop(labels=0, axis=0)
#print(dataset)

time = dataset.iloc[:,0]
#print(time_dict)
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}


t22_5 = [[k, random.uniform(500, 800)] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(1000, 1200)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(1100, 1200)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(1400, 800)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(1300, 1500)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(900, 1100)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
#print(all)
all_df=pd.DataFrame(all, columns=['Date', 'H'])
print(all_df.head(15))

all_cv=all_df.to_csv('H_mar_apr_may_2011.csv', index=False)

input_file = "SH_sep_oct_nov_9_11.xlsx"
dataset = pd.read_excel(input_file)
#dataset = dataset.drop(labels=0, axis=0)
#print(dataset)

time = dataset.iloc[:,0]
#print(time_dict)
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}


t22_5 = [[k, random.uniform(500, 800)] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(1000, 1200)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(1100, 1200)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(1400, 800)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(1300, 1500)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(900, 1100)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
#print(all)
all_df=pd.DataFrame(all, columns=['Date', 'H'])
print(all_df.head(15))

all_cv=all_df.to_csv('H_sep_oct_nov_2011.csv', index=False)

input_file = "SH_jun_jul_aug_6_8.xlsx"
dataset = pd.read_excel(input_file)
#dataset = dataset.drop(labels=0, axis=0)
#print(dataset)

time = dataset.iloc[:,0]
#print(time_dict)
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}


t22_5 = [[k, random.uniform(500, 800)] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(1000, 1200)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(1100, 1200)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(1400, 800)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(1300, 1500)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(900, 1100)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
#print(all)
all_df=pd.DataFrame(all, columns=['Date', 'H'])
print(all_df.head(15))

all_cv=all_df.to_csv('H_jun_jul_aug_2011.csv', index=False)

