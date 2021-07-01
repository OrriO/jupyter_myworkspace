#-*- coding: utf-8 -*-
# @Time    : 2018/12/8 9:33
# @Author  : Z
# @Email   : S
# @File    : 1.1irisDemo.py
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")

# df = sns.load_dataset("iris")
import pandas as pd
df=pd.read_csv(".\\iris.csv")
print(df)
sns.pairplot(df, hue="species")
plt.show()