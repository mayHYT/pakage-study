
def simple_coroutine():
    print("--> start")
    x = yield
    print("---> recieve", x)


sc = simple_coroutine()

print(1111)

next(sc) #预激

print(2222)
sc.send(123)
'''
#生成生成器
g = (x*x for x in range(5))
print(type(g))
'''