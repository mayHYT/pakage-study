
import os
from multiprocessing import Process

def info(title):
    print(title)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id :", os.getpid())


def f(name):
    info("Function f")
    print("hello ", name)

if __name__ == '__main__':
    info("main_line")
    p = Process(target=f, args=('bbb', ))
    p.start()
    p.join()