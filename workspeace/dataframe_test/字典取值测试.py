#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys

# reload(sys)
sys.setdefaultencoding('utf-8')

# print sys.getdefaultencoding()
# wy_hegui_id = {'hg_level1': {
#     '耳鼻咽喉科': '61414',
#     '口腔科': '61416',
#     '眼科': '61415'
# },
#     'hg_level2': {
#         '内分泌科': '6316d7a0-b3d3-4b48-9dce-667d27cc58b7000',
#         '肿瘤科': '78430c83-77b6-4d8b-965c-818d2ee19f1d000',
#         '皮肤科': '728f7f79-f75a-46d6-b4bb-11df3ae8eaad000'
#     }
# }
# print type(wy_hegui_id)
# print wy_hegui_id
# print wy_hegui_id.values()
#
# print json.dumps(wy_hegui_id.values(), encoding='utf-8', ensure_ascii=False)
#
# for i in wy_hegui_id:
#     if i == 'hg_level1':
#         print i
#         print wy_hegui_id[i].get()
#     elif i == 'hg_level1':


dict= {
        '耳鼻咽喉科': '61414',
        '风湿免疫科': '150366b2-91e5-415f-a2ac-fde3c029349d000',
        '妇科': 'ca0a5e2b-b546-4596-bd1b-c704698971cd000',
        '肝胆外科': '9656a49c-3e36-4c12-a2a8-df34c6e60e62000',
        '感染科': 'fac0b801-f369-4e24-abfe-97ef2d04cf2d000',
        '肛肠科': 'f40967c5-c0f3-4d6e-85ec-166ff800dfb7000',
        '骨科': '550d3b0e-e8fb-45f1-a136-d4ee3b257c73000',
        '呼吸内科': '5abe47be-b6b5-4c61-9f9f-e8ccc7c5d1bb000',
        '口腔科': '61416',
        '泌尿外科': '319ca765-1fc7-4821-844f-76351aa986d7000',
        '内分泌科': '6316d7a0-b3d3-4b48-9dce-667d27cc58b7000',
        '皮肤科': '728f7f79-f75a-46d6-b4bb-11df3ae8eaad000',
        '普外科': '17d85eb9-9470-43eb-b2de-606e84dce23b000',
        '乳腺外科': '012bd396-90d7-4375-b0fb-e490e7b251d5000',
        '神经内科': 'ac6be618-7461-4a32-9004-6bd1bae1abfa000',
        '神经外科': '4341d586-66a9-43d2-98c2-70ce1c98d2bd000',
        '肾内科': 'b06697da-1315-461b-a749-3464ca35cb77000',
        '消化内科': '77b4de99-8ad6-442b-8d65-2a2a051ae86c000',
        '小儿内科': '13d6142e-760e-4f04-99ff-c85464649c37000',
        '心血管内科': 'd390e920-b328-4301-96a6-d5b5a853e14f000',
        '心血管外科': '01ac2a9e-3ee9-4493-8b4a-acda491862a8000',
        '胸外科': 'd2a4abfa-b3eb-4cb8-a65c-95d6266359db000',
        '血液科': '9583198c-830d-4151-8574-676ffcc06881000',
        '眼科': '61415',
        '放射科': 'f2759fd5-92cb-4bdf-8420-20b44debc63a000',
        '整形科': 'd1ad63b5-8d34-4c52-8735-f2314f2f6149000',
        '肿瘤科': '61422',
        '精神科': '83f46889-838e-44ed-8368-1cdc68aded77000',
        '心理科': '0a5e1ade-d0b2-47dd-bd4f-769d1ae4110f000',
    }

print dict.get('耳鼻咽喉科')
print dict.get('耳鼻咽喉科')

print type(dict.get('耳鼻咽喉科'))

print '61414'


a="""hsushusisijsj  '%s'"""
b=a % '61414'

# print a
# print b
