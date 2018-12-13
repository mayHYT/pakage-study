
def simple_coroutine(a):
    print("-->start")

    b = yield a
    print("--->recieve", a, b)

    c = yield a+b
    print("--->recieve", a,b,c)


sc = simple_coroutine(9)

aa = next(sc)
print(aa)

bb = sc.send(6)
print(bb)

cc = sc.send(7)
print(cc)
