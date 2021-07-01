#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 16:03
# @Author  : Z
# @Email   : S
# @File    : 18.0seaborn.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set(style="darkgrid")
tips = sns.load_dataset("tips")
#1.处理基础数据
#total_bill和tip关系
# sns.relplot(x="total_bill", y="tip", data=tips);
# sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips);
sns.relplot(x="total_bill", y="tip", hue="smoker",
            col="time", data=tips);
#2.处理时间数据
# df = pd.DataFrame(dict(time=pd.date_range("2017-1-1", periods=500),
#                        value=np.random.randn(500).cumsum()))
# print(df.head())
# g = sns.relplot(x="time", y="value", kind="line", data=df)
# g.fig.autofmt_xdate()
# 3.分类变量
# sns.catplot(x="day", y="total_bill", data=tips);
# sns.catplot(x="day", y="total_bill", hue="sex", kind="swarm", data=tips);
# sns.catplot(x="smoker", y="tip", order=["No", "Yes"], data=tips);
# sns.catplot(x="day", y="total_bill", kind="box", data=tips);
# sns.boxplot(x="day",y="total_bill",hue="smoker",data=tips)
plt.show()