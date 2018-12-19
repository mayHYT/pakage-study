'''
#使用next方法进行迭代
with open(r"test.txt", 'r') as f:
    strchar = next(f)
    while strchar:
        print(strchar, end=' ')
        strchar = next(f)
'''
'''
with open(r"test.txt", 'r') as f:
    strchar = f.__next__()
    while strchar:
        print(strchar, end=' ')
        strchar = f.__next__()
'''
'''
for line in open('test.txt'):
    print(line.upper(), end='')
'''
#列表不是迭代器
L = [1,2,3,4,5]
I = iter(L)
print(iter(L) is L)
while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print(X ** 2, end=' ')

#print(I.__next__())


D = {'a':1, 'b':2, 'c':3}

print(iter(D) is D)

#列表解析式 生成一个新的列表
print(L)
print(id(L))
L = [x+10 for x in L]
print(L)
print(id(L))

#文件中的迭代器
import  string
f = open('test.txt')
line = f.readlines()
print(line)

line = [lines.rstrip() for lines in line]
print(line)

lines = [line.rstrip() for line in open('test.txt')]
print(lines)

#添加条件判断
lines = [line.rstrip() for line in open('test.txt') if line[0] == 'h']
print(lines)

print([x+y for x in 'abc' for y in 'lmn'])

'''
map(str.upper(), open('test.txt'))
print(list(map(str.upper(), open('test.txt'))))
'''
print(max(open('test.txt')))

print('&&'.join(open('test.txt')))

a,b,c = open('test.txt')
print(a,b,c)

print(set(open('test.txt')))


def f(a, b,c):
    print(a,b,c, sep='&')

f(1,2,3)
f(*[1,2,3])
f(*open('test.txt'))

list_ = list(zip('abc','def'))
print(type(list_))
print(list_)

R = range(10)
print(type(R))

I = iter(R)
print(type(I))

