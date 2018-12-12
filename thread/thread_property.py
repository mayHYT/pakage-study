#利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法

import time
import threading


def loop1(in1):
    print('Start loop 1 at :', time.ctime())
    print("param1 is:", in1)
    time.sleep(10)
    print("End loop 1 at:", time.ctime())

def loop2(in1, in2):
    print('Start loop 2 at:', time.ctime())
    print("param1 is", in1, "param2 is", in2)
    time.sleep(20)
    print("End loop 2 at:", time.ctime())

def loop3():
    print("Start loop3 at ", time.ctime())
    time.sleep(15)
    print("End loop3 at ",time.ctime())

def main():
    print("Starting at:",time.ctime())
    #生成threading.thread实例
    t1 = threading.Thread(target=loop1, args=("zhangsan",))
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=("haha", "limei"))
    t2.setName("THR_2")
    t2.start()

    t3 = threading.Thread(target=loop3(), args=())
    t3.setName("THR_3")
    t3.start()

    print("Current running thread's count is {}".format(threading.currentThread()))
    #t1.join()
    #t2.join()
    #预计3秒后，thread2已经自动结束
    time.sleep(1)
    #enumerate 得到正在运行子线程，即子线程1和子线程3
    for thr in threading.enumerate():
        print("Running thread's name is {}".format(thr.getName()))

    print("Running thread'd count is {}".format(threading.activeCount()))

    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)