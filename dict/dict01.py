
D = {'spam':2, 'ham':1, 'eggs':3}
print(D['spam'])
print(D)

#字典的所有方法
for fun in dir(D):
    print(fun)

#打印字典的所有键值, 返回类型是
print(D.keys())
print(type(D.keys()))

#该表字典某个键对应的值
D['ham'] = ['grill', 'back','fry']
print(D)

#删除某个键
del D['eggs']
print(D)

print(D.items())

#判断键是否存在
print(D.get('eggs'))
print(D.get('ham'))

#字典合并
D1 = {'tost':4, 'muffin':7}
D.update(D1)
print(D)

#删除一个键值对
print(D.pop('spam'))
print(D)





