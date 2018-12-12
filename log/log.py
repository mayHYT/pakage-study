#logging 模块
import logging

'''
for func in dir(logging):
    print(func)
'''
LOG_FORMAT = "%(asctime)s %(lineno)d %(levelname)s %(message)s"
#LOG_FORMAT = "%(asctime)s %(lineno)d  %(user)s[%(ip)s] %(levelname)s %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename="log.log", level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("This is debug info.")
logging.info("This is info ")
logging.warning("This is warming info.")
logging.error("This is error info.")
logging.critical("This is critical info.")
logging.info("%s is %d years old", "Tom", 18)
#logging.info("Some one delete the log file.", exc_info=True, stack_info=True, extra={'user':'Tom', 'ip':'10.138.92.147'})


'''
logging.log(logging.DEBUG, "This is debug info")
logging.log(logging.INFO, "This is info message")
logging.log(logging.WARNING, "This is warming info")
logging.log(logging.ERROR, "This is error info")
'''

