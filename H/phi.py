# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:00:06 2022

@author: HP
"""

import pandas as pd
import numpy as np
import re

#input updated file
input_file = pd.read_excel("Updated Mymensingh.xlsx")
input_file = input_file.drop(labels=0, axis=0)
ws = input_file.iloc[:,7].to_list()
wd = input_file.iloc[:,8].to_list()
sr = input_file.iloc[:,12].to_list()
h = input_file.iloc[:,14].to_list()
p = input_file.iloc[:,15].to_list()
date = []
for i in input_file.iloc[:,0]:
    date.append(str(i))
ws_dict = {date[i]:ws[i] for i in range(len(ws))}
wd_dict = {date[i]:wd[i] for i in range(len(wd))}
sr_dict = {date[i]:sr[i] for i in range(len(sr))}
h_dict = {date[i]:h[i] for i in range(len(h))}
p_dict = {date[i]:p[i] for i in range(len(p))}
#P_cond1 = [[i, ws_dict.get(i), wd_dict.get(i), sr_dict.get(i), h_dict.get(i), p_dict.get(i)] for i in ws_dict if ((0<= ws_dict.get(i) <2) & (0<= wd_dict.get(i) <30) & (0<= sr_dict.get(i) <118) & (0<= h_dict.get(i) <=300) & (0.1<= p_dict.get(i) <0.3))]

m12_2_h22_5 = []
m12_2_h6_9 = []
m12_2_h10_12 = []
m12_2_h13_15 = []
m12_2_h16_18 = []
m12_2_h19_21 = []
m3_5_h22_5 = []
m3_5_h6_9 = []
m3_5_h10_12 = []
m3_5_h13_15 = []
m3_5_h16_18 = []
m3_5_h19_21 = []
m6_8_h22_5 = []
m6_8_h6_9 = []
m6_8_h10_12 = []
m6_8_h13_15 = []
m6_8_h16_18 = []
m6_8_h19_21 = []
m9_11_h22_5 = []
m9_11_h6_9 = []
m9_11_h10_12 = []
m9_11_h13_15 = []
m9_11_h16_18 = []
m9_11_h19_21 = []
for i in date:
    #print(i)
    if(re.match("^2021(.|-)(0[1-2]|12)(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((0[0-5]|2[2-3]):00:00)$", i)):
        m12_2_h22_5.append(i)
    elif(re.match("^2021(.|-)(0[1-2]|12)(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((0[6-9]):00:00)$", i)):
        m12_2_h6_9.append(i)
    elif(re.match("^2021(.|-)(0[1-2]|12)(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[0-2]):00:00)$", i)):
        m12_2_h10_12.append(i)
    elif(re.match("^2021(.|-)(0[1-2]|12)(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[3-5]):00:00)$", i)):
        m12_2_h13_15.append(i)
    elif(re.match("^2021(.|-)(0[1-2]|12)(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[6-8]):00:00)$", i)):
        m12_2_h16_18.append(i)
    elif(re.match("^2021(.|-)(0[1-2]|12)(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((19|2[0-1]):00:00)$", i)):
        m12_2_h19_21.append(i)
    elif(re.match("^2021(.|-)(0[3-5])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((0[0-5]|2[2-3]):00:00)$", i)):
        m3_5_h22_5.append(i)
    elif(re.match("^2021(.|-)(0[3-5])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((0[6-9]):00:00)$", i)):
        m3_5_h6_9.append(i)
    elif(re.match("^2021(.|-)(0[3-5])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[0-2]):00:00)$", i)):
        m3_5_h10_12.append(i)
    elif(re.match("^2021(.|-)(0[3-5])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[3-5]):00:00)$", i)):
        m3_5_h13_15.append(i)
    elif(re.match("^2021(.|-)(0[3-5])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[6-8]):00:00)$", i)):
        m3_5_h16_18.append(i)
    elif(re.match("^2021(.|-)(0[3-5])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((19|2[0-1]):00:00)$", i)):
        m3_5_h19_21.append(i)
    elif(re.match("^2021(.|-)(0[6-8])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((0[0-5]|2[2-3]):00:00)$", i)):
        m6_8_h22_5.append(i)
    elif(re.match("^2021(.|-)(0[6-8])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((0[6-9]):00:00)$", i)):
        m6_8_h6_9.append(i)
    elif(re.match("^2021(.|-)(0[6-8])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[0-2]):00:00)$", i)):
        m6_8_h10_12.append(i)
    elif(re.match("^2021(.|-)(0[6-8])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[3-5]):00:00)$", i)):
        m6_8_h13_15.append(i)
    elif(re.match("^2021(.|-)(0[6-8])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[6-8]):00:00)$", i)):
        m6_8_h16_18.append(i)
    elif(re.match("^2021(.|-)(0[6-8])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((19|2[0-1]):00:00)$", i)):
        m6_8_h19_21.append(i)
    elif(re.match("^2021(.|-)(09|1[0-1])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((0[0-5]|2[2-3]):00:00)$", i)):
        m9_11_h22_5.append(i)
    elif(re.match("^2021(.|-)(09|1[0-1])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((0[6-9]):00:00)$", i)):
        m9_11_h6_9.append(i)
    elif(re.match("^2021(.|-)(09|1[0-1])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[0-2]):00:00)$", i)):
        m9_11_h10_12.append(i)
    elif(re.match("^2021(.|-)(09|1[0-1])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[3-5]):00:00)$", i)):
        m9_11_h13_15.append(i)
    elif(re.match("^2021(.|-)(09|1[0-1])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((1[6-8]):00:00)$", i)):
        m9_11_h16_18.append(i)
    elif(re.match("^2021(.|-)(09|1[0-1])(.|-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]) ((19|2[0-1]):00:00)$", i)):
        m9_11_h19_21.append(i)

#(m9_11_h19_21)

def P_Condition(date_list, dic_ws, dic_wd, dic_sr, dic_h, dic_p, n1,n2, h1,h2, ft1,ft2, u1, u2):
    P_cond1 = [i for i in date_list if ((u1<= dic_ws.get(i) <u2) & (n1<= dic_wd.get(i) <n2) & (ft1<= dic_sr.get(i) <ft2) & (h1< dic_h.get(i) <=h2) & (0<= dic_p.get(i) <0.1))]
    P_cond2 = [i for i in date_list if ((u1<= dic_ws.get(i) <u2) & (n1<= dic_wd.get(i) <n2) & (ft1<= dic_sr.get(i) <ft2) & (h1< dic_h.get(i) <=h2) & (0.1<= dic_p.get(i) <0.2))]
    P_cond3 = [i for i in date_list if ((u1<= dic_ws.get(i) <u2) & (n1<= dic_wd.get(i) <n2) & (ft1<= dic_sr.get(i) <ft2) & (h1< dic_h.get(i) <=h2) & (0.2<= dic_p.get(i) <0.3))]
    P_cond4 = [i for i in date_list if ((u1<= dic_ws.get(i) <u2) & (n1<= dic_wd.get(i) <n2) & (ft1<= dic_sr.get(i) <ft2) & (h1< dic_h.get(i) <=h2) & (0.3<= dic_p.get(i) <0.4))]
    return [P_cond1, P_cond2, P_cond3, P_cond4]

def frequency(li):
    count = [len(i) for i in li]
    return count
#0,30,60,90,120,150,180,210,240,270,300,330
u1=2.0
u2=3.4
n1=0.0
n2=30.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')

u1=2.0
u2=3.4
n1=30.0
n2=60.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')

u1=2.0
u2=3.4
n1=60.0
n2=90.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')

u1=2.0
u2=3.4
n1=90.0
n2=120.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')

u1=2.0
u2=3.4
n1=120.0
n2=150.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')

u1=2.0
u2=3.4
n1=150.0
n2=180.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')


u1=2.0
u2=3.4
n1=180.0
n2=210.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')

u1=2.0
u2=3.4
n1=210.0
n2=240.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')

u1=2.0
u2=3.4
n1=240.0
n2=270.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')


u1=2.0
u2=3.4
n1=270.0
n2=300.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')


u1=2.0
u2=3.4
n1=300.0
n2=330.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')

u1=2.0
u2=3.4
n1=330.0
n2=360.0
h1=1500
h2=1600
ft1=700.0
ft2=950.0
a1 = P_Condition(m12_2_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b1 = frequency(a1)
#print("b1", b1)
a2 = P_Condition(m12_2_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b2 = frequency(a2)
a3 = P_Condition(m12_2_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a3)
b3 = frequency(a3)
#print(
a4 = P_Condition(m12_2_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a4)
b4 = frequency(a4)
#print(b4)
a5 = P_Condition(m12_2_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a5)
b5 = frequency(a5)
#print(b5)
a6 = P_Condition(m12_2_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
#print(a6)
b6 = frequency(a6)
#print(b6)
a7 = P_Condition(m3_5_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b7 = frequency(a7)
#print(b7)
a8 = P_Condition(m3_5_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b8 = frequency(a8)
#print(b8)
a9 = P_Condition(m3_5_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b9 = frequency(a9)
#print(b9)
a10 = P_Condition(m3_5_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b10 = frequency(a10)
#print(b10)
a11 = P_Condition(m3_5_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b11 = frequency(a11)
#print(b11)
a12 = P_Condition(m3_5_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b12 = frequency(a12)
#print(b12)
a13 = P_Condition(m6_8_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b13 = frequency(a13)
#print(b13)
a14 = P_Condition(m6_8_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b14 = frequency(a14)
#print(b14
a15 = P_Condition(m6_8_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b15 = frequency(a15)
#print(b15)
a16 = P_Condition(m6_8_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b16 = frequency(a16)
#print(b16)
a17 = P_Condition(m6_8_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b17 = frequency(a17)
#print(b17)
a18 = P_Condition(m6_8_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b18 = frequency(a18)
#print(b18)
a19 = P_Condition(m9_11_h22_5, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b19 = frequency(a19)
#print(b19)
a20 = P_Condition(m9_11_h6_9, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b20 = frequency(a20)
#print(b20)
a21 = P_Condition(m9_11_h10_12, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b21 = frequency(a21)
#print(b21)
a22 = P_Condition(m9_11_h13_15, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b22 = frequency(a22)
#print(b22)
a23 = P_Condition(m9_11_h16_18, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b23 = frequency(a23)
#print(b23)
a24 = P_Condition(m9_11_h19_21, ws_dict, wd_dict, sr_dict, h_dict, p_dict, n1, n2, h1, h2, ft1,ft2, u1, u2)
b24 = frequency(a24)
#print(b24)
e=[]
for i in range(4):
    d = [b1[i],b2[i],b3[i],b4[i],b5[i],b6[i],b7[i],b8[i],b9[i],b10[i],b11[i],b12[i],b13[i],b14[i],b15[i],b16[i],b17[i],b18[i],b19[i],b20[i],b21[i],b22[i],b23[i],b24[i]]
    e.append(d)
#print(e)
p0 = [[u1, n1, ft1, h2, 0.0, sum(e[0])] + e[0]]
f0 = [i for w in p0 for i in w]
#print(f0)
p1 = [[u1, n1, ft1, h2, 0.1, sum(e[1])] + e[1]]
f1 = [i for w in p1 for i in w]
#print(f1)
p2 = [[u1, n1, ft1, h2, 0.2, sum(e[2])] + e[2]]
f2 = [i for w in p2 for i in w]
#print(f2)
p3 = [[u1, n1, ft1, h2, 0.3, sum(e[3])] + e[3]]
f3 = [i for w in p3 for i in w]
p0 = [p0+e[0]]
f = [f0,f1,f2,f3]
df = pd.DataFrame(f)
df.iloc[:,0] = df.iloc[:,0].apply(lambda x: "{:},".format(x))
df.iloc[:,1] = df.iloc[:,1].apply(lambda x: "{:},".format(x))
df.iloc[:,2] = df.iloc[:,2].apply(lambda x: "{:},".format(x))
df.iloc[:,3] = df.iloc[:,3].apply(lambda x: "{:}.,".format(x))
df.iloc[:,4] = df.iloc[:,4].apply(lambda x: "{:},".format(x))
df.iloc[:,29] = df.iloc[:,29].apply(lambda x: "{:}.".format(x))
for i in range(5,29):
    df.iloc[:,i] = df.iloc[:,i].apply(lambda x: "{:}.,".format(x))
print(df)

#df = df.to_csv("phi_s.txt", index=False, header=False, sep=' ')

df = df.to_csv("new file.txt", index=False, header=False, sep='\t', mode='a+')
