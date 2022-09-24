# -*- coding: utf-8 -*-
"""
Created on Sun May  8 15:25:23 2022

@author: Eutech
"""

import pandas as pd
import numpy as np
import datetime
import random

from datetime import datetime

input_file = "SH_dec_jan_feb_12_2.xlsx"
dataset = pd.read_excel(input_file)
time = dataset.iloc[:,0]
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}

#t22_5 = [[k, np.random.choice([0, 1, 1.5, 2, 3.5, 4.5], size=(1,), p=[7./12, 3./12, 1./12, 1./24, 3./120, 2./120])] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
#t22_5 = [[k, np.random.choice([0, 0.5, 0.86], size=(1,), p=[4./6, 1./6, 1./6])] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t22_5 = [[k, random.uniform(2,6)] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(2,6)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(2,6)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(2,6)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(3,6)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(3,6)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
all_df=pd.DataFrame(all, columns=['Date', 'WS'])
print(all_df.head(30))
all_cv=all_df.to_csv('WS_dec_feb_2020.csv', index=False)

input_file = "SH_mar_apr_may_3_5.xlsx"
dataset = pd.read_excel(input_file)
time = dataset.iloc[:,0]
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}
t22_5 = [[k, np.random.choice([4.4364, 7.6890, 15.7869], size=(1,), p=[4./6, 1./6, 1./6])] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, np.random.choice([5.44, 7.246, 12.4377], size=(1,), p=[4./6, 1./6, 1./6])] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(2,10)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, np.random.choice([5.54679, 8.347, 11.2179], size=(1,), p=[4./6, 1./6, 1./6])] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, np.random.choice([4.5436, 7.56, 11.45], size=(1,), p=[5./6, 1./12, 1./12])] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(2.34, 10.45)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
all_df=pd.DataFrame(all, columns=['Date', 'WS'])
print(all_df.head(30))
all_cv=all_df.to_csv('WS_mar_may_2020.csv', index=False)

input_file = "SH_jun_jul_aug_6_8.xlsx"
dataset = pd.read_excel(input_file)
time = dataset.iloc[:,0]
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}
t22_5 = [[k, np.random.choice([3.554, 3.756967, 10.2155, 12.658, 3.756987, 10.45736], size=(1,), p=[7./12, 3./12, 1./12, 1./24, 4./120, 1./120])] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(2.34, 10.543)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(2.34, 10.45)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(2.34,  5.45)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(2.34, 5.05)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(2.34, 10.45)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
all_df=pd.DataFrame(all, columns=['Date', 'WS'])
print(all_df.head(30))
all_cv=all_df.to_csv('WS_jun_aug_2020.csv', index=False)

input_file = "SH_sep_oct_nov_9_11.xlsx"
dataset = pd.read_excel(input_file)
time = dataset.iloc[:,0]
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}
t22_5 = [[k, np.random.choice([3.53454, 5.4576, 6.43668], size=(1,), p=[4./6, 1./6, 1./6])] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(2.134, 5.568)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(4.134, 5.556)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(2.134, 5.556)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(2.134, 5.55)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(2.134, 5.556)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
all_df=pd.DataFrame(all, columns=['Date', 'WS'])
print(all_df.head(30))
all_cv=all_df.to_csv('WS_sep_nov_2020.csv', index=False)