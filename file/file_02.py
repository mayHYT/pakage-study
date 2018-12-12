myfile = open('myfile.txt', 'w')
myfile.write("hello txt file. \n")
myfile.write("goodbye txt file. \n")
myfile.close()

'''
myfile = open('myfile.txt')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
'''

'''
#用文件迭代器打印文件内容
for line in open('myfile.txt'):
    print(line)

x,y,z = 44,45,46
S = 'spam'
D = {'a':1, 'b':2}
L = [1,2,3]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' %(x,y,z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

F = open('datafile.txt')
line = F.readline()
print(line)
print(line.rstrip())

line = F.readline()
print(line)
part = line.split(',')
print(part)

#将列表中的字符转化为整数
number = [int(p) for p in part]
print(number)
line = F.readline()
print(line)
part = line.split('$')
print(part)
print(eval(part[0]))

objects = [eval(p) for p in part]
print(objects)
'''
#pickle 模块能够存储python原生对象
import _pickle

dict = {'one': 1, 'two':2, 'three':3}
F = open('datafile.txt', 'wb')
_pickle.dump(dict, F)
F.close()

F = open('datafile.txt', 'rb')
E = _pickle.load(F)
print(E)

print(type(dir(F)))
for value in dir(F):
    print(value)

