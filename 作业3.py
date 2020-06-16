# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:17:13 2020

@author: zhaoxinrui
"""


import pandas as pd
import numpy as np

result = pd.read_csv('car_complain.csv')
print(result)

result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
print(result)

#品牌投诉总数
df1= result.groupby(['brand'])['id'].agg(['count'])
print(df1)

#车型投诉总数
df2= result.groupby(['car_model','brand'])['id'].agg(['count'])
print(df2)

#哪个品牌的平均车型投诉最多(各品牌总投诉词条数/各品牌车型数)
df2.reset_index(inplace=True)
print(df2)
df3= df2.groupby(['brand'])['car_model'].agg(['count'])
print(df3)
df4= df1.merge(df3,left_index=True, right_index=True, how='left')
print(df4)
df4['average']= df4.apply(lambda x:x[1]/x[0],axis=1)
print(df4)
df5= df4.sort_values(by='average',ascending=False)
print(df5)

#哪个品牌的平均车型投诉最多（各品牌总投诉拆分到每个问题的个数/各品牌车型数）
result['total']= result.iloc[:,7:180].sum(axis=1)
print(result.columns)
df6= result.groupby(['brand'])['total'].agg(['sum'])
print(df6)
df7= df3.merge(df6,left_index=True, right_index=True, how='left')
df7['average']= df7.apply(lambda x:x[1]/x[0],axis=1)
df7= df7.sort_values(by='average',ascending=False)
print(df7)