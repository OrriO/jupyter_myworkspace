#!/usr/bin/python
# -*- coding: utf-8 -*-


import collections
import codecs
import math
import re
# from utils import illegal
smooth = 0
import os
path1=os.path.abspath('.')

def illegal(s):
    return not s or s == '' or s == 'undefined' or s == '(null)' or s == 'NULL'



name = '/data/test.csv'
user_click_list = collections.defaultdict(list)
for line in codecs.open(name,'r',encoding='utf8'):
    line = line.strip()
    s_split = line.split(',')
    if len(s_split) != 4:
        continue
    user_id,expert_id,cnt,_ = s_split
    if illegal(user_id) or \
            illegal(expert_id):
        continue
    if illegal(cnt):
        comment_cnt = smooth
    user_click_list[user_id].append((expert_id,int(cnt)))

new_list = {}
for k,v in user_click_list.items():
    new_list[k] = [x[0] for x in sorted(v,key=lambda x:x[1],reverse=True)[:10]]

pattern = re.compile(r'[:|]?')

def read_recoms(name):
    recom_list = collections.defaultdict(list)
    for line in codecs.open(name,'r',encoding='utf8'):
        line = line.strip()
        s_split = line.split(',')
        user_id = s_split[0]
        for s in s_split[1:]:
            result = pattern.split(s)
            if len(result) == 3:
                disease_id, expert_id, cnt = result
                recom_list[user_id].append(expert_id)
    return recom_list



cfcbf_name = 'test2.csv'
cfcbf_recom_list = read_recoms(cfcbf_name)


cfcbf_users = cfcbf_recom_list.keys()

on_users = user_click_list.keys()


print(len(on_users))

#计算覆盖率


cfcbf_on_users = cfcbf_users & on_users
print(len(cfcbf_on_users),len(cfcbf_users | on_users))

# 单个用户的推荐准确度


def cal_user_score(users,recom_list,click_list):
    result = []
    for user in users:
        recoms = recom_list[user][:20]
        clicks = click_list[user]
        join = set(recoms) & set(clicks)
        union = set(recoms) | set(clicks)

        recoms_index = sorted([recoms.index(x) for x in join])
        clicks_index = sorted([clicks.index(x) for x in join])

        recoms_avg = clicks_avg = lds = 0.0

        if recoms_index and clicks_index:

            recoms_avg = sum([1.0/(x+1) for x in recoms_index])/len(recoms_index)*1.0
            clicks_avg = sum([1.0/(x+1) for x in clicks_index])/len(clicks_index)*1.0
            # 参考：https://blog.csdn.net/Eyizoha/article/details/89420549
            lds = 0.0
            for index in range(0,len(join)):
                lds += (recoms_index[index] - clicks_index[index])**2
            lds = lds/len(join)
            
        result.append((user,len(join),len(union),recoms_avg,clicks_avg,lds))
    return result



f = codecs.open('cfcbf_user_score.csv','w',encoding='utf8')
cf_result = cal_user_score(cfcbf_on_users,cfcbf_recom_list,new_list)
for x in cf_result:
    user,ljoin,lunion,recoms_avg,clicks_avg,lds = x
    f.write("%s,%.10f,%.10f,%.10f,%.10f,%.10f\n" %(user,ljoin,lunion,recoms_avg,clicks_avg,lds))

