stm = lambda x : x * 100

print(stm(10))

stm1 = lambda x,y,z:(x+y)*100*z
print(stm1(12,19,8))

def funA(n):
    print("Function A ...")
    return n * 100
'''
#函数名是一个变量
funB = funA
funB()
'''
def funC(n, f):
    return f(n) * 3

print(funC(3, funA))

from functools import reduce

def myAdd(x, y):
    return x+y

ret = reduce(myAdd, [1,2,3,4,5,6])
print(ret)

#filter案例


#返回值是函数
def myF2():

    def myF3():
        print("In myF3....")
        return 3
    return myF3

f3=myF2()
print(type(f3))
print(f3)
f3()

#闭包
def count():
    fs = []
    for i in range(1,4):
        #定义一个函数
        #f是一个闭包结构
        def f():
            return i*i
        fs.append(f)
        #print("i = {}".format(i))
        #print(fs[i])
    return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())


def count1():
    def f(j):
        def g():
            return j*j
        return g

    fs1 = []
    for i in range(1,4):
        #定义一个函数
        #f是一个闭包结构
        fs1.append(f(i))
        #print("i = {}".format(i))
        #print(fs[i])
    return fs1
f1,f2,f3=count1()
print(f1())
print(f2())
print(f3())

#装饰器
import time

def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return f(*args, **kwargs)
    return wrapper

@printTime
def hello():
    print("Hello world ...")

hello()

print("*" *20)
#手动执行装饰器
def hello3():
    print("manual operator ...")

h3 = printTime(hello3)
h3()

l = printTime(hello3)
l()

#偏函数
print(type(int("14567")))

def int2(x, base=2):
    return int(x, base)

print(int2('10010'))

import functools

int2 = functools.partial(int, base=2)

print(int2('1010'))



def modo(n,m):
    return n%m

mod100 = functools.partial(modo, 100)
print(mod100(7)