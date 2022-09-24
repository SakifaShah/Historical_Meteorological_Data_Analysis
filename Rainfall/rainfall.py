# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:58:50 2022

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
t22_5 = [[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
all_df=pd.DataFrame(all, columns=['Date', 'RF'])
print(all_df.head(30))
all_cv=all_df.to_csv('RF_dec_feb_2020.csv', index=False)

input_file = "SH_mar_apr_may_3_5.xlsx"
dataset = pd.read_excel(input_file)
time = dataset.iloc[:,0]
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}
t22_5 = [[k, np.random.choice([0, 0.46, 0.323], size=(1,), p=[4./6, 1./6, 1./6])] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, np.random.choice([0, 0.02, 0.15], size=(1,), p=[5./6, 1./12, 1./12])] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, np.random.choice([0, 0.03, 0.016], size=(1,), p=[5./6, 1./12, 1./12])] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
all_df=pd.DataFrame(all, columns=['Date', 'RF'])
print(all_df.head(30))
all_cv=all_df.to_csv('RF_mar_may_2020.csv', index=False)

input_file = "SH_jun_jul_aug_6_8.xlsx"
dataset = pd.read_excel(input_file)
time = dataset.iloc[:,0]
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}
t22_5 = [[k, np.random.choice([0, 1, 1.01, 1.59, 3, 4], size=(1,), p=[7./12, 3./12, 1./12, 1./24, 4./120, 1./120])] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
all_df=pd.DataFrame(all, columns=['Date', 'RF'])
print(all_df.head(30))
all_cv=all_df.to_csv('RF_jun_aug_2020.csv', index=False)

input_file = "SH_sep_oct_nov_9_11.xlsx"
dataset = pd.read_excel(input_file)
time = dataset.iloc[:,0]
date = [int(i.strftime("%H")) for i in time]
time_dict = {i: int(i.strftime("%H")) for i in time}
t22_5 = [[k, np.random.choice([0, 0.33, 0.17], size=(1,), p=[4./6, 1./6, 1./6])] for k, i in time_dict.items() if(i==22 or i==23 or i==0 or i==1 or i==2 or i==3 or i==4 or i==5)]
t6_9=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==6 or i==7 or i==8 or i==9)]
t10_12=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==10 or i==11 or i==12)]
t13_15=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==13 or i==14 or i==15)]
t16_18=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==16 or i==17 or i==18)]
t19_21=[[k, random.uniform(0,0)] for k, i in time_dict.items() if(i==19 or i==20 or i==21)]
all = t22_5 + t6_9 + t10_12 + t13_15 + t16_18 + t19_21
all_df=pd.DataFrame(all, columns=['Date', 'RF'])
print(all_df.head(30))
all_cv=all_df.to_csv('RF_sep_nov_2020.csv', index=False)