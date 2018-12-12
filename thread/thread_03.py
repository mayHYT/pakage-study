#利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法

import time
import _thread as thread


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
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thead
    # 参数两个，一个是需要运行的函数名，第二是函数的参数作为元祖使用，为空则使用空元祖
    # 注意：如果函数只有一个参数，需要参数后由一个逗号
    thread.start_new_thread(loop1, ("zhangsan", ))
    thread.start_new_thread(loop2, ("lili", "Lucia"))
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)