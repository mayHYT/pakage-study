import threading
import time

#1.类需要继承自threading.Thread
class Mythread(threading.Thread):
    def __init__(self, arg):
        super(Mythread, self).__init__()
        self.arg = arg

    #2.必须重写run函数，run函数代表的是真正执行的功能
    def run(self):
        time.sleep(2)
        print("The arg for this class is {}".format(self.arg))

for i in range(5):
    t = Mythread(i)
    t.start()
    t.join()

print("Main thread done ....")
