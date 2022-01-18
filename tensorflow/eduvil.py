from pickletools import optimize
import numpy as np
import tensorflow as tf
import pandas as pd

data = pd.read_excel('aaa.xlsx')
tmp_lms = []
list = []
result = []

for i, rows in data.iterrows():
    if(i > 1):
        tmp_lms.append([rows['Unnamed: 1'],rows['자기주도'],rows['Unnamed: 5'],
                rows['Unnamed: 6'],rows['Unnamed: 8'],rows['Unnamed: 9'],
                rows['Unnamed: 10'],rows['Unnamed: 11'],rows['Unnamed: 12'],
                rows['Unnamed: 13'],rows['Unnamed: 14']])

for i in tmp_lms:
    flag = True
    for j in i:
        if pd.isna(j):
            flag = False
            break
    if flag == True:
        list.append(i)
        
for i in list:
    flag = True
    num = 0
    for j in i:
        if type(j) == int or type(j) == float:
            num += j
    if flag == True:
        result.append([i[0],num/(len(i)-1)])
        
# print(result)
# print("count", count)

print(result)

