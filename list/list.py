# '+'号两边必须是相同类型的
list = [1,2,3,4]+[4,5,6,7]
print(list)

'''
list = [7,8,9]+"abc"
print(list)
'''
#列表解析式创建列表
res = [c*4 for c in 'SPAM']
print(res)

'''
#map
list(map(abs, [1,2,-4,5]))
print(list)
'''

L = ['spam','spam1','spam2']
L1 = L[1:]
print(id(L))
print(id(L1))
print(L1)

L[1] = 'eggs'
print(L)
L[0:2] = ['eat', 'more']
print(L)
L.append('hello')
print(L)
#排序
L.sort()
print(L)

#列表可以追加一个对象
l={'klv':1,'ktv':2}
L.append(l)
print(L)




