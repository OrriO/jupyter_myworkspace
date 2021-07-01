a = [1, 2, 3, 4]
b = [3, 4, 5]

c = len(set(b).intersection(set(a)))
print(c)

print(type('["3a23bf0a-ebe7-4d73-8c4e-692a10575e04000","fde5073f-6da8-480b-a130-3ab052a503eb000"]'))
d = '["3a23bf0a-ebe7-4d73-8c4e-692a10575e04000","fde5073f-6da8-480b-a130-3ab052a503eb000"]'
f = '["3a23bf0a-ebe7-4d73-8c4e-692a10575e04000"]'
# str_list = list(map(int, (d.split('[')[1].split(']')[0]).resplace(" ", "")))
# print(str_list)

# e=map(int,d.split('[')[1].split(']')[0])
# print(e)
e = len(set(eval(f)).intersection(set(eval(d))))
print(e)

# >>> str = '[1, 2, 3, 4]'
# >>> str_list = eval(str)
# >>> str_list
# [1, 2, 3, 4]
# >>> type(str_list)
# <class 'list'>


('116659846',
 '56195407',
 '68783437',
 '122062903',
 '122208361',
 '123538768',
 '123922248',
 '123949591',
 '14724969',
 '52438870',
 '68765924',
 '80734810',
 '12369275',
 '15616996',
 '122987265',
 '124044050',
 '68985481',
 '25286759',
 '71524876',
 '72541036')
