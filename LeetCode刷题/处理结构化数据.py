import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
from IPython.display import display

from sys import version_info  #检查python的版本
if version_info.major != 3:
    raise Exception('Please use the version 2 to finish the project')

pd.set_option('display.max_columns' , None)   # 显示所有列
pd.set_option('display.max_rows' , None) # 显示所有行

lianjia_df = pd.read_csv('lianjia.csv')
display(lianjia_df.head(n=10))     #展示前10行的数据
lianjia_df.info()
print(lianjia_df.describe())    #描述性统计值(平均数，标准差，中位数，最小值，最大值，25%分位数，75%分位数)

#添加新特征房屋价格
df = lianjia_df.copy()
df ['PerPrice'] = lianjia_df['Price']/lianjia_df['Size']

#调整列的顺序
colums = ['Region' ,'PerPrice', 'District' , 'Garden' , 'Layout' , 'Floor' , 'Year' , 'Size' , 'Elevator','Derection','Renovation' ]
df = pd.DataFrame(df, columns = colums)  #pandas数据帧dataframe....https://www.yiibai.com/pandas/python_pandas_dataframe.html
#显示更新后的数据
display(df.head(n=10))

#数据可视化分析
#根据区域特征，分析不同区域房价和数量的对比
df_region_count = df.groupby('Region')['Price'].count().sort_values(ascending=False).to_frame().reset_index()

