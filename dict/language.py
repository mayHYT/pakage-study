
table = {'python':'Guido van Rossum',
         'Perl':'Larry Wall',
         'Tcl': 'John Ousterhout'}

language = 'python'
creator = table[language]
print(type(creator))

for lang in table:
    print(lang, '\t', table[lang])

#报错
'''
L = []
L[99]='spam'
'''

D = {}
D[99] = 'spam'
print(D)

#字典用于稀疏数据结构
Maxtrix ={}
Maxtrix[(2,3,4)] = 88
Maxtrix[(7,8,9)] = 99

print(Maxtrix)

#避免missing-key错误
try:
    print(Maxtrix[(2,3,6)])
except KeyError:
    print("No this Key")

#当读取嵌套操作元素时，只要简单地把索引操作串起来就可以了
mel = {'name':'Mark',
       'jobs':['trainer', 'write'],
       'web':'www.baidu.com',
       'home':{'state':'CD', 'zip':87690}}

print(mel['name'])
print(mel['jobs'][1])
print(mel['home']['state'])

#创建字典
print(dict.fromkeys(['a','b','c'],0))

#用zip创建列表
print(list(zip(['c','d','e'], [1,2,3])))
#用zip创建字典
D = dict(zip(['a','b','c'],[1,2,3]))
print(D)

#字典解析式创建字典-1
D = {k:v for(k,v) in zip(['l','o','v'],[1,2,3])}
print(D)
#字典解析式创建字典-2
D = {x : x**2 for x in [1,2,3,4]}
print(D)

#键值排序
D = {'c':2, 'b':3, 'a':4}
Ks = D.keys()
for k in sorted(Ks):
    print(k, D[k])

#hash_key 方法已死：in永生
print('c' in D)
print(D.get('d'))
if D.get('a') != None:
    print('present', D['a'])
