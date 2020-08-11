#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[10]:


import numpy as np
import pandas as pd
import csv
import math
import os
import matplotlib.pyplot as plt
import sys
import time
    
def input_df(records):
    # input data
    print(records)
    raw_data = pd.read_csv(records, delimiter='\t')
    data = raw_data.fillna(value = 0)
    data = data.drop([0])
    # categories data 分不同通訊商,生成多個表格
    global list_df
    data["Packet"] = data["Packet"].astype("category")
    df = data["Packet"].cat.categories
    df_Packet = data.groupby("Packet")
    names = globals() #全局命名 for 動態變數名
    list_df=[]
    for i in df:
        list_df.append('df_{x}'.format(x = i))
        names['df_{x}'.format(x = i)] = df_Packet.get_group('{x}'.format(x = i)) #跟據group分拆多個表格
        names['df_{x}'.format(x = i)] = names['df_{x}'.format(x = i)].reset_index().drop('index', axis=1)
    return
    
# RMS : Field Strength E [V/m]  計算部分
def get_rms(records):
    records = records.astype(float)
    result = sum([x ** 2 for x in records])# / len(records)
    result = math.sqrt(result)
    return result

# Field Level [dBµV/m] 計算部分
def Field_Level(records):
    records = records.astype(float)
    result = 20*np.log10(records) + 120
    result = pd.DataFrame(result)
    result.columns = ['Field Level']
    return result

#concat 合併分析資料
def concat_df(records):
    result = pd.concat([records,Field_Level(records["Equiv.FieldStrength"])],axis = 1)
    result = result.append([{'Packet':'Total','Total Field Strength (RMS)':get_rms(records["Equiv.FieldStrength"])}], ignore_index=True)
    result = result.fillna(value = 0)
    return result

#output
def output_df(records):
    for i in records:
#         print(concat_df(eval(i))) #eval()用来计算在字符串中的有效Python表达式,并返回一个对象
        concat_df(eval(i)).to_csv('output_{x}.csv'.format(x = i), encoding='utf-8')
  
input_df('CHINA_mob.Peak.Compressed')
output_df(list_df)


# fig = plt.figure(figsize=(12, 10))
# x = plt.subplot(111)
# x.scatter(data_set['Frequency'], data_set['Equiv.FieldStrength'], c="#62d97b", s=50, marker="+") 
# x.set_xlabel('X'), x.set_ylabel('Y'), x.set_title("title");
# plt.legend(['Cluster 1'])
# plt.grid(True)
# plt.show()

# df.to_csv('excel_to_python.csv')
#data.info(memory_usage="deep")


# In[ ]:





# In[ ]:




