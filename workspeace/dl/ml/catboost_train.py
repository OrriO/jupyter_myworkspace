from datetime import datetime, date, timedelta
import time
import numpy as np
import pandas as pd
import time
import sys
sys.path.append('/home/wangning1')
import os
import findspark
findspark.init('/usr/local/spark-2.3-bin-hadoop-2.6.0-cdh5.8.2')
import pyspark
from pyspark.sql import *
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import *
from pyspark.sql.types import StringType,FloatType,DoubleType,ArrayType
from ai_utils.spark_ope import spark_operate

# 建立spark连接
spark = SparkSession.builder.appName("prefer_train").config("hive.metastore.uris","thrift://10.20.180.199:9083"
         ).config("master","yarn"
         ).config('spark.deploy-mode', "client"
         ).config('spark.yarn.queue', "root.aidata"
         ).config("spark.executor.memory","30g"
         ).config("spark.driver.memory","10g").enableHiveSupport().getOrCreate()

from sklearn.model_selection import train_test_split,KFold
from sklearn.metrics import accuracy_score,roc_auc_score,roc_curve,auc
from sklearn.metrics import classification_report
from catboost import CatBoostClassifier, FeaturesData, Pool, cv
import lightgbm as lgb

# 加载数据
train_df= sparks.to_pandas(spark.sql('''select * from wedw_tmp.tdl_price_tmp2 
where create_date >= '2020-10-01' and create_date <= '2020-12-20' 
and life_seg rlike 
--'专家问诊'
'引入期|非问诊成长期|问诊成长期'
'''),100)
verify_df= sparks.to_pandas(spark.sql('''select * from wedw_tmp.tdl_price_tmp2 
where create_date > '2020-12-20' 
and life_seg rlike  
--'专家问诊'
'引入期|非问诊成长期|问诊成长期'
'''),100)


def target_trans(input_target,input_df):
    range_list = ['[0,20)','[20,50)','[50,100)','[100,200)','[200,+)']
    if input_target == 'multi':
        target_dict = {'[0,20)':1,'[20,50)':2,'[50,100)':3,'[100,200)':4,'[200,+)':5}
    else:
        target_dict = {'[0,20)':0,'[20,50)':0,'[50,100)':0,'[100,200)':0,'[200,+)':0}
        target_dict[range_list[int(input_target)-1]] = 1
    return input_df['price_range'].map(target_dict)


# 区分类别型特征和数值型特征
num_features = ['user_age','is_health_user_id','have_cert'
                ,'hcoin_cnt'
                ,'patient_cnt','patient_age_cnt','patient_actl_cnt','min_patient_age','max_patient_age'
                ,'is_health_vip','spec_exp_range'
                ,'discount_amt','min_threshold','coupon_cnt','max_discount_amt','min_discount_amt','max_min_threshold','min_min_threshold'
                ,'1_weight_99','1_weight_0','1_weight_20','1_weight_50','1_weight_100','1_weight_150','1_weight_200','3_weight_99','3_weight_0','3_weight_20','3_weight_50','3_weight_100','3_weight_150','3_weight_200','7_weight_99','7_weight_0','7_weight_20','7_weight_50','7_weight_100','7_weight_150','7_weight_200','15_weight_99','15_weight_0','15_weight_20','15_weight_50','15_weight_100','15_weight_150','15_weight_200','30_weight_99','30_weight_0','30_weight_20','30_weight_50','30_weight_100','30_weight_150','30_weight_200','90_weight_99','90_weight_0','90_weight_20','90_weight_50','90_weight_100','90_weight_150','90_weight_200','200_weight_99','200_weight_0','200_weight_20','200_weight_50','200_weight_100','200_weight_150','200_weight_200','365_weight_99','365_weight_0','365_weight_20','365_weight_50','365_weight_100','365_weight_150','365_weight_200','1_browse_99','1_click_99','1_follow_99','1_consume_99','1_browse_0','1_click_0','1_follow_0','1_consume_0','1_browse_20','1_click_20','1_follow_20','1_consume_20','1_browse_50','1_click_50','1_follow_50','1_consume_50','1_browse_100','1_click_100','1_follow_100','1_consume_100','1_browse_150','1_click_150','1_follow_150','1_consume_150','1_browse_200','1_click_200','1_follow_200','1_consume_200','3_browse_99','3_click_99','3_follow_99','3_consume_99','3_browse_0','3_click_0','3_follow_0','3_consume_0','3_browse_20','3_click_20','3_follow_20','3_consume_20','3_browse_50','3_click_50','3_follow_50','3_consume_50','3_browse_100','3_click_100','3_follow_100','3_consume_100','3_browse_150','3_click_150','3_follow_150','3_consume_150','3_browse_200','3_click_200','3_follow_200','3_consume_200','7_browse_99','7_click_99','7_follow_99','7_consume_99','7_browse_0','7_click_0','7_follow_0','7_consume_0','7_browse_20','7_click_20','7_follow_20','7_consume_20','7_browse_50','7_click_50','7_follow_50','7_consume_50','7_browse_100','7_click_100','7_follow_100','7_consume_100','7_browse_150','7_click_150','7_follow_150','7_consume_150','7_browse_200','7_click_200','7_follow_200','7_consume_200','15_browse_99','15_click_99','15_follow_99','15_consume_99','15_browse_0','15_click_0','15_follow_0','15_consume_0','15_browse_20','15_click_20','15_follow_20','15_consume_20','15_browse_50','15_click_50','15_follow_50','15_consume_50','15_browse_100','15_click_100','15_follow_100','15_consume_100','15_browse_150','15_click_150','15_follow_150','15_consume_150','15_browse_200','15_click_200','15_follow_200','15_consume_200','30_browse_99','30_click_99','30_follow_99','30_consume_99','30_browse_0','30_click_0','30_follow_0','30_consume_0','30_browse_20','30_click_20','30_follow_20','30_consume_20','30_browse_50','30_click_50','30_follow_50','30_consume_50','30_browse_100','30_click_100','30_follow_100','30_consume_100','30_browse_150','30_click_150','30_follow_150','30_consume_150','30_browse_200','30_click_200','30_follow_200','30_consume_200','90_browse_99','90_click_99','90_follow_99','90_consume_99','90_browse_0','90_click_0','90_follow_0','90_consume_0','90_browse_20','90_click_20','90_follow_20','90_consume_20','90_browse_50','90_click_50','90_follow_50','90_consume_50','90_browse_100','90_click_100','90_follow_100','90_consume_100','90_browse_150','90_click_150','90_follow_150','90_consume_150','90_browse_200','90_click_200','90_follow_200','90_consume_200','200_browse_99','200_click_99','200_follow_99','200_consume_99','200_browse_0','200_click_0','200_follow_0','200_consume_0','200_browse_20','200_click_20','200_follow_20','200_consume_20','200_browse_50','200_click_50','200_follow_50','200_consume_50','200_browse_100','200_click_100','200_follow_100','200_consume_100','200_browse_150','200_click_150','200_follow_150','200_consume_150','200_browse_200','200_click_200','200_follow_200','200_consume_200','365_browse_99','365_click_99','365_follow_99','365_consume_99','365_browse_0','365_click_0','365_follow_0','365_consume_0','365_browse_20','365_click_20','365_follow_20','365_consume_20','365_browse_50','365_click_50','365_follow_50','365_consume_50','365_browse_100','365_click_100','365_follow_100','365_consume_100','365_browse_150','365_click_150','365_follow_150','365_consume_150','365_browse_200','365_click_200','365_follow_200','365_consume_200'
                ,'1_searchclick_weight_0','1_searchclick_weight_20','1_searchclick_weight_50','1_searchclick_weight_100','1_searchclick_weight_150','1_searchclick_weight_200','3_searchclick_weight_0','3_searchclick_weight_20','3_searchclick_weight_50','3_searchclick_weight_100','3_searchclick_weight_150','3_searchclick_weight_200','7_searchclick_weight_0','7_searchclick_weight_20','7_searchclick_weight_50','7_searchclick_weight_100','7_searchclick_weight_150','7_searchclick_weight_200','15_searchclick_weight_0','15_searchclick_weight_20','15_searchclick_weight_50','15_searchclick_weight_100','15_searchclick_weight_150','15_searchclick_weight_200','30_searchclick_weight_0','30_searchclick_weight_20','30_searchclick_weight_50','30_searchclick_weight_100','30_searchclick_weight_150','30_searchclick_weight_200','90_searchclick_weight_0','90_searchclick_weight_20','90_searchclick_weight_50','90_searchclick_weight_100','90_searchclick_weight_150','90_searchclick_weight_200','200_searchclick_weight_0','200_searchclick_weight_20','200_searchclick_weight_50','200_searchclick_weight_100','200_searchclick_weight_150','200_searchclick_weight_200','365_searchclick_weight_0','365_searchclick_weight_20','365_searchclick_weight_50','365_searchclick_weight_100','365_searchclick_weight_150','365_searchclick_weight_200'
                ,'200_gh_payable_amt','200_jswz_payable_amt','200_wzrelate_payable_amt','200_highprice_payable_amt','200_other_payable_amt','200_gh_actual_amt','200_jswz_actual_amt','200_wzrelate_actual_amt','200_highprice_actual_amt','200_other_actual_amt','200_gh_pay_cnt','200_jswz_pay_cnt','200_wzrelate_pay_cnt','200_highprice_pay_cnt','200_other_pay_cnt','200_gh_actl_cnt','200_jswz_actl_cnt','200_wzrelate_actl_cnt','200_highprice_actl_cnt','200_other_actl_cnt','200_gh_pay_atv','200_jswz_pay_atv','200_wzrelate_pay_atv','200_highprice_pay_atv','200_other_pay_atv','200_gh_actl_atv','200_jswz_actl_atv','200_wzrelate_actl_atv','200_highprice_actl_atv','200_other_actl_atv','30_gh_payable_amt','30_jswz_payable_amt','30_wzrelate_payable_amt','30_highprice_payable_amt','30_other_payable_amt','30_gh_actual_amt','30_jswz_actual_amt','30_wzrelate_actual_amt','30_highprice_actual_amt','30_other_actual_amt','30_gh_pay_cnt','30_jswz_pay_cnt','30_wzrelate_pay_cnt','30_highprice_pay_cnt','30_other_pay_cnt','30_gh_actl_cnt','30_jswz_actl_cnt','30_wzrelate_actl_cnt','30_highprice_actl_cnt','30_other_actl_cnt','30_gh_pay_atv','30_jswz_pay_atv','30_wzrelate_pay_atv','30_highprice_pay_atv','30_other_pay_atv','30_gh_actl_atv','30_jswz_actl_atv','30_wzrelate_actl_atv','30_highprice_actl_atv','30_other_actl_atv'
                ,'200_zjwz_payable_amt','200_zjwz_actual_amt','200_zjwz_pay_cnt','200_zjwz_actl_cnt','200_zjwz_pay_atv','200_zjwz_actl_atv','30_zjwz_payable_amt','30_zjwz_actual_amt','30_zjwz_pay_cnt','30_zjwz_actl_cnt','30_zjwz_pay_atv','30_zjwz_actl_atv']
# ,'1_1_weight','1_2_weight','1_3_weight','1_1_accu_weight','1_2_accu_weight','1_3_accu_weight','3_1_weight','3_2_weight','3_3_weight','3_1_accu_weight','3_2_accu_weight','3_3_accu_weight','7_1_weight','7_2_weight','7_3_weight','7_1_accu_weight','7_2_accu_weight','7_3_accu_weight','15_1_weight','15_2_weight','15_3_weight','15_1_accu_weight','15_2_accu_weight','15_3_accu_weight','30_1_weight','30_2_weight','30_3_weight','30_1_accu_weight','30_2_accu_weight','30_3_accu_weight','90_1_weight','90_2_weight','90_3_weight','90_1_accu_weight','90_2_accu_weight','90_3_accu_weight','200_1_weight','200_2_weight','200_3_weight','200_1_accu_weight','200_2_accu_weight','200_3_accu_weight','365_1_weight','365_2_weight','365_3_weight','365_1_accu_weight','365_2_accu_weight','365_3_accu_weight'

cat_features = ['gender_name','phone_province_id','phone_city_id'
                ,'os_lst3m_most','phone_model_lst3m_most','phone_manufacturers_lst3m_most'
                ,'disease_label_lv3_1_id','disease_label_lv3_2_id','disease_label_lv3_3_id','disease_label_lv5_1_id','disease_label_lv5_2_id','disease_label_lv5_3_id','hospital_label_1_id','hospital_label_2_id','hospital_label_3_id','dept_label_1_id','dept_label_2_id','dept_label_3_id'
                ,'doctor_label_1_id','doctor_label_2_id','doctor_label_3_id'
                ,'1_1_range','1_2_range','1_3_range','3_1_range','3_2_range','3_3_range','7_1_range','7_2_range','7_3_range','15_1_range','15_2_range','15_3_range','30_1_range','30_2_range','30_3_range','90_1_range','90_2_range','90_3_range','200_1_range','200_2_range','200_3_range','365_1_range','365_2_range','365_3_range']
# ,'disease_label_lv3_1_name','disease_label_lv3_2_name','disease_label_lv3_3_name','disease_label_lv5_1_name','disease_label_lv5_2_name','disease_label_lv5_3_name','hospital_label_1_name','hospital_label_2_name','hospital_label_3_name','dept_label_1_name','dept_label_2_name','dept_label_3_name'


# 定义特征变量
features = num_features + cat_features
X_origin = train_df[features]
X_offline = verify_df[features]
# 特征类型处理
X_origin[num_features] = X_origin[num_features].astype('int')
X_origin[cat_features] = X_origin[cat_features].astype('category')
cat_features_index = np.where(X_origin.dtypes != np.int)[0]
X_offline[num_features] = X_offline[num_features].astype('int')
X_offline[cat_features] = X_offline[cat_features].astype('category')
# 定义目标变量
target_list = ['multi','1','2','3','4','5']
for each in target_list:
    train_df['target_{0}'.format(each)] = target_trans(each,train_df)
    verify_df['target_{0}'.format(each)] = target_trans(each,verify_df)

# 定义模型训练方法
def model_train(target_string,params,threshold_float=None):
    # 实现变量动态命名
    name = locals()
    
    # 定义目标变量
    Y_origin = train_df['target_'+target_string].astype('int')
    Y_offline = verify_df['target_'+target_string].astype('int')
    
    # 划分测试集
    X, X_test, Y, Y_test = train_test_split(X_origin, Y_origin, test_size=0.0000001, random_state=0)##test_size测试集所占比例
    # 划分训练集和验证集
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.2, random_state=0)##test_size验证集所占比例

    # 数据预处理
    train_pool = Pool(X_train, Y_train, cat_features = cat_features_index)
    validate_pool = Pool(X_validation, Y_validation, cat_features=cat_features_index)
    offline_pool = Pool(X_offline, Y_offline, cat_features=cat_features_index)

    # 初始化模型
    name['model_' + target_string] = CatBoostClassifier(**params)

    # 模型训练
    model_tmp = name['model_' + target_string]
    model_tmp.fit(train_pool, eval_set=validate_pool)

    if target_string == 'multi':
        # 输出验证集效果
        name[target_string + '_v']  = classification_report(Y_validation, model_tmp.predict(X_validation), target_names=['1','2','3','4','5'])
#         # 输出测试集效果
#         name[target_string + '_t'] = classification_report(Y_test, model_tmp.predict(X_test), target_names=['1','2','3','4','5'])
        # 输出离线评估效果
        name[target_string + '_o'] = classification_report(Y_offline, model_tmp.predict(X_offline), target_names=['1','2','3','4','5'])
    else:
        # 界定阈值输出验证集效果报告
        name['Y_' + target_string + '_v'] = np.array([int(i[1]>=threshold_float) for i in model_tmp.predict_proba(X_validation)])
        name[target_string + '_v'] = classification_report(Y_validation, name['Y_' + target_string + '_v'], target_names=['0','1'])
#         # 界定阈值输出测试集效果报告
#         name['Y_' + target_string + '_t'] = np.array([int(i[1]>=threshold_float) for i in model_tmp.predict_proba(X_test)])
#         name[target_string + '_t'] = classification_report(Y_test, name['Y_' + target_string + '_t'], target_names=['0','1'])
        # 界定阈值输出离线评估效果报告
        name['Y_' + target_string + '_o'] = np.array([int(i[1]>=threshold_float) for i in model_tmp.predict_proba(X_offline)])
        name[target_string + '_o'] = classification_report(Y_offline, name['Y_' + target_string + '_o'], target_names=['0','1'])       

    # 输出效果报告
    print('verify_report:/n' + name[target_string + '_v'])
#     print('test_report:/n' + name[target_string + '_t'])
    print('offline_report:/n' + name[target_string + '_o'])

    # 保存模型文件
    # name['model_' + target_string].save_model(r'/home/ai/notebook/wangning/user_fertility/user_fertility_' + target_string + r'.model')
    
    train_df['pretarget_{0}'.format(target_string)] = [i[1] for i in model_tmp.predict_proba(train_df[features])]
    verify_df['pretarget_{0}'.format(target_string)] = [i[1] for i in model_tmp.predict_proba(verify_df[features])]
    
    return name['model_' + target_string]


# 二分类模型2
params2 = {
        'learning_rate': 0.07,
        'early_stopping_rounds': 450,
        'iterations': 500,
        'random_seed': 6,
        'depth': 5,
        'loss_function': 'Logloss',
        'eval_metric':'AUC'
        }
model_2 = model_train('2',params2,0.5)     