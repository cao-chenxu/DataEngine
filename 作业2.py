# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:51:10 2020

@author: 赵
"""


import pandas as pd
from pandas import Series, DataFrame
data = {'Chinese': [66, 95, 93, 90,80],'English': [65, 85, 92, 88, 90],'Math': [30, 98, 96, 77, 90]}
df1= DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)
print (df2.describe())
print(df2.describe().loc[['mean','min','max','std'],])
df3= df2.describe().loc[['mean','min','max','std'],]
print(df3)
df4=df3.append(df2.var().rename('var'))
print(df4)

print(df2.var())

total = df2.sum(axis=1).sort_values(ascending=False)
print(total)

