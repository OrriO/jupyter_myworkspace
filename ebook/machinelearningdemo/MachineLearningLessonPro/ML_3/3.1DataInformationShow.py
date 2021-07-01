# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 14:43
# @Author  : Z
# @Email   : S
# @File    : 3.0DataInformation.py
import pandas as pd
import os

# 1.导入数据文件
datapath = os.path.join(".", "train.csv")
talentData = pd.read_csv(datapath, sep=",")
# 2.绘制一些基本数据图形
import seaborn as sns
import matplotlib.pyplot as plt


def show_education():
    # 2.1分析离职和受教育程度的分析
    sns.countplot(x="Attrition", hue="Education", data=talentData)
    plt.show()
def showBoxplot():
    plt.figure(figsize=(20, 20))
    plt.subplot(221)
    # 1.离职和年龄的关系
    sns.boxplot(x="Attrition", y="Age", data=talentData)
    # 2.离职和家庭和距离之间的关系
    plt.subplot(222)
    sns.boxplot(x="Attrition", y="DistanceFromHome", data=talentData)
    # 3.离职和月收入的关系
    plt.subplot(223)
    sns.boxplot(x="Attrition", y="MonthlyIncome", data=talentData)
    # 4.离职和曾经工作公司的关系
    plt.subplot(224)
    sns.boxplot(x="Attrition", y="NumCompaniesWorked", data=talentData)
    plt.show()


def showGender():
    fig = plt.figure(figsize=(15, 15))
    fig.add_subplot(211)
    # 离职和婚姻状况分析
    sns.countplot(x="Attrition", hue="MaritalStatus", data=talentData)
    fig.add_subplot(212)
    # 离职和性别关系
    sns.countplot(x="Attrition", hue="Gender", data=talentData)
    plt.show()


def showPairplot():
    sns.pairplot(talentData, hue="Attrition", height=3,
                 vars=["Age", "WorkLifeBalance",
                       "DistanceFromHome", "Education",
                       "StandardHours"])
    plt.show()


if __name__ == '__main__':
    # show_education()
    # showBoxplot()
    # showGender()
    showPairplot()
