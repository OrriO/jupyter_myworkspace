#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 16:10
# @Author  : Z
# @Email   : S
# @File    : 19.0tantanincSave.py
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

titanic = sns.load_dataset("titanic")
# sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic);
# sns.catplot(x="deck", kind="count", palette="ch:.25", data=titanic);
sns.catplot(y="deck", hue="class", kind="count",
            palette="pastel", edgecolor=".6",
            data=titanic);
plt.show()