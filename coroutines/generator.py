#如何生成一个生成器
#直接使用
#如果函数中包含yield，则这个函数就叫生成器
#next调用函数，遇到yield返回
def odd(a):
    print("Step 1")
    yield a

    print("Step 2")
    yield a+1

    print("Step 3")
    yield a + 2

g = odd(7)

one = next(g)
print(one)

two = next(g)
print(two)

three = next(g)
print(three)
