
with open(r'test.txt','r') as f:
    l = list(f)
    for line in l:
        print(line)

print("*"* 20)

with open(r"test.txt", 'r') as f:
    strchar = f.read(1)
    while strchar:
        print(strchar, end=' ')
        strchar = f.read(1)



#tell函数：用来显示文件读写指针的当前位置

with open(r'test.txt', 'r') as f:
    str = f.read(3)
    pos = f.tell()

    while str:
        print(pos)
        print(str)

        str = f.read(3)
        pos = f.tell()



#文件的写操作
#向文件追加一行
#a 表示以追加方式打开
with open(r'test.txt', 'a') as f:
    f.write("life is not only has beautiful \nbut also unhappy things.")

#writelines 参数可以是list格式
with open(r'test.txt', 'a') as f:
    f.writelines("today is very cold ")
    f.writelines("I am so unhappy")

l = ['I', 'love', 'may']

with open(r'test.txt', 'w') as f:
    f.writelines(l)

'''
#pickle 序列化案例
import pickle

age = 24

with open(r'test.txt', 'wb') as f:
    pickle.dump(age, f)

'''



























