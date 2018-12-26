import numpy as np
import pandas as pd
df = pd.DataFrame([10, 20, 30, 40],columns = ['Numbers'],index = ['a', 'b', 'c', 'd'])
print(df)

df1 = pd.DataFrame([10, 20, 30, 40], \
                  columns = ['Numbers'], \
                  index = ['a', 'b', 'c', 'd'])
print(df1.index)     #显示索引 show index
print(df1.columns)    #显示列名 show column names
print(df1.ix['c'])     #通过索引选择  select via index
print(df1.ix[['a', 'd']])  # 多选 multi-select
print(df1.ix[df1.index[1:3]])  # 其他another
print(df1.sum())   # 每列求和  sum per column
ts = df1 ** 2    # 创建新的DataFrame create new DataFrame
print(ts)

df2 = pd.DataFrame([10, 20, 30, 40], \
                  columns = ['Numbers'], \
                  index = ['a', 'b', 'c', 'd'])

#add a new column called 'floats' directly
df2['floats'] = (1.5, 2.5, 3.5, 4.5)

#add a new column called 'names' by index
df2['names'] = pd.DataFrame(['Dan', \
                            'Cox', 'Ale', 'Bob'], \
                            index = ['d', 'c', 'a', 'b'])
# add a new object to df
df2 = df2.append(pd.DataFrame({ \
               'Numbers':66, 'floats':5.5, \
               'names':'Yor'}, index=['y',]))