# import nltk
# nltk.download('stopwords')
#
from nltk.corpus import stopwords
s=stopwords.words('english')

if 'by' in s:
    print(1)


# a='digitoxin metabolism by rat liver microsomes.'
#
# # b= a.split(' ')
# # print(b)
# c=[['radiochemical', 'assay', 'of', 'g', 'and', 'its', 'rat', 'liver', 'in', 'vivo.'],
#    ['digitoxin', 'metabolism', 'by', 'rat', 'liver', 'microsomes.']]
# d=['of','in','g','by']
#
# for k,v in enumerate(c):
#     v=[w for w in v if w not in d]
#     c[k]=v
#     print(v)
#     print(c)