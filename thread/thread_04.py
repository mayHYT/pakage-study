#利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法

import time
import threading


def loop1(in1):
    print('Start loop 1 at :', time.ctime())
    print("param1 is:", in1)
    time.sleep(4)
    print("End loop 1 at:", time.ctime())

def loop2(in1, in2):
    print('Start loop 2 at:', time.ctime())
    print("param1 is", in1, "param2 is", in2)
    time.sleep(2)
    print("End loop 2 at:", time.ctime())

def main():
    print("Starting at:",time.ctime())
    #生成threading.thread实例
    t1 = threading.Thread(target=loop1, args=("zhangsan",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("haha", "limei"))
    t2.start()

    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)