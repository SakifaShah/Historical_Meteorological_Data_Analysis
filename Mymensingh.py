# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:32:59 2022

@author: HP
"""

# importing the module
import pandas as pd
import numpy as np

#input file 
input_file = "Mymensingh.xlsx"
dataset = pd.read_excel(input_file)
print(type(dataset))

# negatives, zeros remove
def weather(df, n, col_name, cond):
    df = df.drop(labels=0, axis=0)
    #contains only SO2 value
    df_X_ = df.iloc[:,n]
    
    #contains date and value
    df_X = df.iloc[:,[0,n]]
    #df_X = df_X.fillna(0)
    df_X = df_X.fillna(-1)
    #df_X = df_X.fillna(2000)
    
    #list to store date and value
    val = []
    values = []
    
    for i, v in df_X.itertuples(index=False):
        float_val = float(v)
        
        #Condition SO2 >500
        #Condition NOX >500
        #Condition PM25 >500
        #Condition PM10 >600
        #Condition RH >100
        #Condition Temp >50 , NUll -- DayNight
        
        #Condition CO >300
        #Condition WS >100
        #Condition WD >360
        #Condition VWR >100
        
# =============================================================================
#         if (float_val<=0 or float_val>=cond):
#             float_val = "Null"
# =============================================================================
# =============================================================================
        if (float_val<0 or float_val>=cond):
             float_val = "Null"
        
        else:
            values.append(float_val)
        val.append((i,float_val))
# =============================================================================

# =============================================================================
#         if (float_val>=cond):
#             float_val = "Null"
# =============================================================================
        
    
    average_value = sum(values) / len(values)
    
    df_X = pd.DataFrame(val, columns=['Date', col_name])
    df_X = df_X.replace("Null", average_value)
    return df_X


# =============================================================================
# BP = weather(dataset, 13, "BP_Mymensingh", 1020)
# print(BP)
# BP = BP.to_csv('BP_Mymensingh.csv', index=False)
# =============================================================================

# =============================================================================
# CO = weather(dataset, 5, "CO_Mymensingh", 300)
# print(CO)
# CO = CO.to_csv('CO_Mymensingh.csv', index=False)
# 
# WS = weather(dataset, 9, "WS_Mymensingh", 100)
# print(WS)
# WS = WS.to_csv('WS_Mymensingh.csv', index=False)
# 
# WD = weather(dataset, 10, "WD_Mymensingh", 360)
# print(WD)
# WD = WD.to_csv('WD_Mymensingh.csv', index=False)
# 
# VWS = weather(dataset, 15, "VWS_Mymensingh", 100)
# print(VWS)
# VWS = VWS.to_csv('VWS_Mymensingh.csv', index=False)

O3 = weather(dataset, 6, "O3_Mymensingh", 400)
print(O3)
O3 = O3.to_csv('O3_Mymensingh.csv', index=False)
# =============================================================================


# =============================================================================
# SR = weather(dataset, 14, "SR_Mymensingh", 2000)
# print(SR)
# SR = SR.to_csv('SR_Mymensingh.csv', index=False)
# 
# =============================================================================
# =============================================================================
# # =============================================================================
# =============================================================================
# SO2 = weather(dataset, 1, "SO2_Mymensingh", 500)
# print(SO2)
# SO2 = SO2.to_csv('SO2_Mymensingh.csv', index=False)
# 
# NOX = weather(dataset, 4, "NOX_Mymensingh", 500)
# print(NOX)
# NOX = NOX.to_csv('NOX_Mymensingh.csv', index=False)
# 
# PM10 = weather(dataset, 7, "PM10_Mymensingh", 600)
# print(PM10)
# PM10 = PM10.to_csv('PM10_Mymensingh.csv', index=False)
#  
# =============================================================================
# PM25 = weather(dataset, 8, "PM25_Mymensingh", 500)
# print(PM25)
# PM25 = PM25.to_csv('PM25_Mymensingh.csv', index=False)
# =============================================================================
# =============================================================================

# =============================================================================
# RH = weather(dataset, 12, "RH_Mymensingh", 100)
# print(RH)
# RH = RH.to_csv('RH_Mymensingh.csv', index=False)
# =============================================================================

# =============================================================================
# =============================================================================
# TEMP = weather(dataset, 11, "TEMP_Mymensingh", 50)
# print(TEMP)
# TEMP = TEMP.to_csv('TEMP_Mymensingh.csv', index=False)
# =============================================================================
#     
# =============================================================================
