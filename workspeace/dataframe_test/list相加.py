#!/usr/bin/python
#-*- coding: utf-8 -*- 


index_dict = {
    'basic_index': ['expert_id', 'hdf_expert_id', 'expert_name'],
    'professional_index': ['rank_state', 'hosp_level', 'dept_level', 'academic_leader', 'committee_member',
                           'expert_level'],
    'web_effect_index': ['patient_cnt', 'patient_apply_cnt', 'avg_reply_time', 'praise_rate', 'like_cnt',
                         'registration_reputation_rate', 'total_pv', 'hosp_niq', 'other_influence']
}

c=index_dict.get('basic_index')+['patient_cnt', 'patient_apply_cnt', 'avg_reply_time', 'praise_rate', 'like_cnt',
                         'registration_reputation_rate', 'total_pv', 'hosp_niq', 'other_influence']
print c
print type(c)